from rest_framework import serializers

from accounts.api.serializers import AccountSerializer
from products.api.serializers import ProductSerializer
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"