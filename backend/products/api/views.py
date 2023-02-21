import re
from django.db.models import Q, Count
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from products.api.serializers import ProductSerializer, CategorySerializer, ManufacturerSerializer
from products.models import Product, Category, Manufacturer
from reviews.api.serializers import ReviewSerializer


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = []

    def get_queryset(self, obj):
        return Product.objects.filter(num_available__gt=0)

    def list(self, request):
        min_price = self.request.query_params.get('minPrice')
        max_price = self.request.query_params.get('maxPrice')
        manufacturer = self.request.query_params.get('manufacturer').split(',') \
            if self.request.query_params.get('manufacturer') else None
        category = self.request.query_params.get('category')
        subcategory = self.request.query_params.get('subcategory').split(',') \
            if self.request.query_params.get('subcategory') else None
        grams = self.request.query_params.get('grams').split(',') if self.request.query_params.get('grams') else None
        sorting = self.request.query_params.get('sorting')
        query = self.request.query_params.get('q')

        queryset = Product.objects.all()
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if manufacturer:
            queryset = queryset.filter(manufacturer__name__in=manufacturer)
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if subcategory:
            queryset = queryset.filter(Q(category__name__in=subcategory) & Q(category__parent__name__iexact=category))
        if grams:
            filtered_grams = [re.search(r'\d+', i).group(0) for i in grams if i != 'większe']
            if 'większe' in grams:
                queryset = queryset.filter(grams_weight__gt=1000)
            queryset = queryset.filter(grams_weight__in=filtered_grams)
        if query:
            queryset = queryset.filter(name__icontains=query)
        if sorting:
            sorting_type = 'price'
            if sorting == '0':
                sorting_type = 'price'
            elif sorting == '1':
                sorting_type = '-price'
            queryset = queryset.order_by(sorting_type)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, slug=None):
        item = get_object_or_404(Product, slug=slug)
        product = ProductSerializer(item)
        reviews = ReviewSerializer(item.reviews.all(), many=True)
        data = product.data | {'reviews': reviews.data}
        return Response(data)


class ProductLatestListView(APIView):
    model = Product
    serializer_class = ProductSerializer(many=True)
    authentication_classes = []

    def get(self, request):
        queryset = Product.objects.all()[:4]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductBestsellersListView(APIView):
    model = Product
    serializer_class = ProductSerializer(many=True)
    authentication_classes = []

    def get(self, request):
        queryset = Product.objects.annotate(orders_count=Count('orders')).order_by('-orders_count')[:4]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class SingleProductView(viewsets.ViewSet):
    authentication_classes = []

    def retrieve(self, request, pk=None):
        item = get_object_or_404(Product, pk=pk)
        product = ProductSerializer(item)
        reviews = ReviewSerializer(item.reviews.all(), many=True)
        data = product.data | {'reviews': reviews.data}
        return Response(data)


class CategoryViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryMainViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = Category.objects.filter(parent=None).all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ManufacturerViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
        return Response(serializer.data)
