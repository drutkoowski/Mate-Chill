from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from orders.models import Order
from reviews.api.serializers import ReviewSerializer
from reviews.models import Review


class ReviewViewSet(ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset = Review.objects.order_by('-created_at').all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data.copy()
        data['author'] = request.user.pk
        is_bought = Order.objects.filter(~Q(status='nieopłacone'), user__pk=request.user.pk, products__product=data['product']).exists()
        serializer = ReviewSerializer(data=data)
        if is_bought:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({
                             'message': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'You have not bought this item.'},
            status=status.HTTP_400_BAD_REQUEST)