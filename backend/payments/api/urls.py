from django.urls import path
from payments.api import views

app_name = "payments"


urlpatterns = [
    # path("orders/",
    #      views.OrderViewSet.as_view({'get': 'list'}),
    #      name='orders'),
    path("create-session/", views.CreateCheckoutSession.as_view(), name='create-session'),
    path('webhook-test/', views.WebHook.as_view()),
]
