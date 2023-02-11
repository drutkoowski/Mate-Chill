from django.urls import path

from products.api import views

app_name = "products"

urlpatterns = [
    path('products/', views.ProductViewSet.as_view({'get': 'list'}), name="products"),
    path('products/<slug:slug>', views.ProductViewSet.as_view({'get': 'retrieve'}), name="product-detail"),
]