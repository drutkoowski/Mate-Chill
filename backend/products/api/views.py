from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.api.serializers import ProductSerializer, CategorySerializer, ManufacturerSerializer
from products.models import Product, Category, Manufacturer


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = []

    def get_queryset(self, obj):
        return Product.objects.filter(num_available__gt=0)

    def list(self, request):
        min_price = self.request.query_params.get('minPrice') if self.request.query_params.get('minPrice') else None
        max_price = self.request.query_params.get('maxPrice') if self.request.query_params.get('maxPrice') else None
        manufacturer = self.request.query_params.get('manufacturer').split(',') \
            if self.request.query_params.get('manufacturer') else None
        category = self.request.query_params.get('category').split(',') if self.request.query_params.get('category') \
            else None
        grams = self.request.query_params.get('grams').split(',') if self.request.query_params.get('grams') else None
        print(min_price, max_price, manufacturer, category, grams)
        from rest_framework.pagination import PageNumberPagination
        queryset = Product.objects.all()
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if manufacturer:
            queryset = queryset.filter(manufacturer__name__in=manufacturer)
        if category:
            queryset = queryset.filter(category__name__in=category)

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
        serializer = ProductSerializer(item)
        return Response(serializer.data)


class ProductLatestListView(APIView):
    model = Product
    serializer_class = ProductSerializer(many=True)
    authentication_classes = []

    def get(self, request):
        queryset = Product.objects.all()[:4]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ManufacturerViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
        return Response(serializer.data)
