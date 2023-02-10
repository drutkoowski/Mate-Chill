from django.urls import path

from accounts.api import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name="register"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]
