from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from orders.api.serializers import OrderSerializer

from orders.models import Order, OrderProduct
from products.models import Product


class OrderViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Order.objects.filter(user__pk=request.user.pk).order_by('-created_at').all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(Order, pk=pk, user=request.user)
        serializer = OrderSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        data['data']['user'] = request.user.pk
        serializer = OrderSerializer(data=data['data'])
        serializer.is_valid(raise_exception=True)
        products = list(data['products'])
        if products:
            serializer.save()
            for product in products:
                product_obj = Product.objects.get(pk=product['id'])
                product_obj.num_available -= product['count']
                product_obj.save()
                OrderProduct.objects.create(product=product_obj, count=product['count'], order=serializer.instance)
            serializer.instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
