from rest_framework import serializers

from orders.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ('status', 'summary_cost', 'shipping_cost', 'total_product_cost',)

    def get_products(self, obj):
        try:
            queryset = obj.products.all()
            serializer = OrderSerializer(queryset, many=True)
            return serializer.data
        except:
            return []