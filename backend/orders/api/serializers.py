from rest_framework import serializers

from orders.models import Order, OrderProduct
from products.api.serializers import ProductSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = OrderProduct
        fields = "__all__"

    def get_product(self, obj):
        serializer = ProductSerializer(obj.product)
        return serializer.data


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ('status', 'summary_cost', 'shipping_cost', 'total_product_cost',)

    def get_products(self, obj):
        try:
            queryset = obj.products.all()
            serializer = OrderProductSerializer(queryset, many=True)
            return serializer.data
        except:
            return []

    def get_created_at(self, obj):
        date = obj.created_at.strftime("%d-%m-%Y")
        return date