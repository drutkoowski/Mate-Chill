from django.urls import path

from products.api import views

app_name = "products"

urlpatterns = [
    path('products/',
         views.ProductViewSet.as_view({'get': 'list'}),
         name="products"),
    path('products/latest',
         views.ProductLatestListView.as_view(),
         name="latest"),
    path('products/<slug:slug>',
         views.ProductViewSet.as_view({'get': 'retrieve'}),
         name="product-detail"),
    path('categories/',
         views.CategoryViewSet.as_view({'get': 'list'}),
         name='categories'
         ),
    path('categories/main',
         views.CategoryMainViewSet.as_view({'get': 'list'}),
         name='main-categories'
         ),
    path('manufacturers/',
         views.ManufacturerViewSet.as_view({'get': 'list'}),
         name="manufacturers"),
]