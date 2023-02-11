from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from products.api.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny,]

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