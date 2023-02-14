from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from products.models import Product, Category, Manufacturer


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "slug", "subcategories",)

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    manufacturer = ManufacturerSerializer()
    link = serializers.URLField(source='get_absolute_url')

    class Meta:
        model = Product
        fields = "__all__"
