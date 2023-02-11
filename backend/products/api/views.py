from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from products.api.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny,]

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        item = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(item)
        return Response(serializer.data)