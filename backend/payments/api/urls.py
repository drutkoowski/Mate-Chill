from django.urls import path
from payments.api import views

app_name = "payments"


urlpatterns = [
    path("create-session/", views.CreateCheckoutSession.as_view(), name='create-session'),
    path('webhook/', views.WebHook.as_view()),
]
