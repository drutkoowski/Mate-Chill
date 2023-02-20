from django.urls import path
from reviews.api import views

app_name = 'reviews'

urlpatterns = [
    path("",
         views.ReviewViewSet.as_view({'get': 'list'}),
         name='list'),
    path("create",
         views.ReviewViewSet.as_view({'post': 'create'}),
         name='create'),
]