from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenBlacklistSerializer

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "phone", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5}
        }

    def create(self, validated_data) -> Account:
        account = get_user_model().objects.create_user(**validated_data)

        return account


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    """Overwiritten validate behaviour for cookies."""
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get(
            "refresh"
        )
        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken("No valid token found in cookie")


class CookieTokenBlacklistSerializer(TokenBlacklistSerializer):
    """Overwritten validate function behaviour for jwt in cookies."""
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get(
            "refresh"
        )
        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken("No valid token found in cookie")
