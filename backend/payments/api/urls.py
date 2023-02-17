from django.urls import path
from payments.api import views

app_name = "payments"


urlpatterns = [
    # path("orders/",
    #      views.OrderViewSet.as_view({'get': 'list'}),
    #      name='orders'),
    path("secret/", views.secret)
]
