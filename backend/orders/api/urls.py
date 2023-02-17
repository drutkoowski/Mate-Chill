from django.urls import path
from orders.api import views

app_name = "orders"


urlpatterns = [
    path("orders/",
         views.OrderViewSet.as_view({'get': 'list'}),
         name='orders'),
    path("orders/<int:pk>",
         views.OrderViewSet.as_view({'get': 'retrieve'}),
         name='order'),
    path("order/create",
         views.OrderViewSet.as_view({'post': 'create'}),
         name='create-order'),
]
