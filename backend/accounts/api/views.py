from typing import Union
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from accounts.api.serializers import AccountSerializer, CookieTokenRefreshSerializer, CookieTokenBlacklistSerializer
from mate import settings


class CreateUserView(generics.CreateAPIView):
    serializer_class = AccountSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self) -> Union[AbstractBaseUser, AnonymousUser]:
        return self.request.user


class MyTokenObtainPairView(TokenObtainPairView):
    """
    API view to log in - create JWT access and refresh tokens and place them into cookie.
    Takes request with user credentials, credentials check against database and if correct returns
    JWT access and refresh tokens placed into hhtponly cookies.
    Remove access abd refresh JWT's from response body.
    The idea here is to persist token at client side in the cookie not
    in the local storage therefore protect JWTs against access by javascripts/ XSS.
    """

    def post(self, request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        tokens = response.data
        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=tokens[settings.SIMPLE_JWT["AUTH_COOKIE"]],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )
        response.set_cookie(
            key=settings.SIMPLE_JWT["REFRESH_COOKIE"],
            value=tokens[settings.SIMPLE_JWT["REFRESH_COOKIE"]],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )

        # Remove tokens from response body for enchanced security.
        del response.data[settings.SIMPLE_JWT["AUTH_COOKIE"]]
        del response.data[settings.SIMPLE_JWT["REFRESH_COOKIE"]]

        return response


class MyTokenRefreshView(TokenRefreshView):

    def finalize_response(
            self, request, response, *args, **kwargs
    ) -> Response:
        tokens = response.data
        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=tokens[settings.SIMPLE_JWT["AUTH_COOKIE"]],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )
        # Remove tokens from response body for enchanced security.
        del response.data[settings.SIMPLE_JWT["AUTH_COOKIE"]]
        del response.data[settings.SIMPLE_JWT["REFRESH_COOKIE"]]

        return super().finalize_response(
            request, response, *args, **kwargs
        )

    serializer_class = CookieTokenRefreshSerializer


class MyTokenBlacklistView(TokenBlacklistView):

    def finalize_response(
            self, request, response, *args, **kwargs
    ) -> Response:
        # Remove tokens from response body for enchanced security.
        response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE"])
        response.delete_cookie(settings.SIMPLE_JWT["REFRESH_COOKIE"])

        return super().finalize_response(
            request, response, *args, **kwargs
        )

    serializer_class = CookieTokenBlacklistSerializer
