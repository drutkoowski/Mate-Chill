from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.api.serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]

    def get_queryset(self, obj):
        return Product.objects.filter(num_available__gt=0)

    def list(self, request):
        from rest_framework.pagination import PageNumberPagination
        queryset = Product.objects.all()

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
    permission_classes = [AllowAny, ]

    def get(self, request):
        queryset = Product.objects.all()[:4]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        # popular_categories = queryset.filter(pro)
        return Response(serializer.data)
