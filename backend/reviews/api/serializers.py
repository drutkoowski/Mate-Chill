from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from accounts.api.serializers import AccountSerializer
from accounts.models import Account
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = SerializerMethodField(read_only=True)
    created_at = SerializerMethodField()

    class Meta:
        model = Review
        fields = "__all__"

    def get_created_at(self, obj):
        date = obj.created_at.strftime("%d-%m-%Y")
        return date

    def get_author(self, obj):
        return AccountSerializer(obj.author).data

    def validate(self, attrs):
        author = Account.objects.get(pk=self.initial_data.get('author'))
        attrs['author'] = author
        return super().validate(attrs)