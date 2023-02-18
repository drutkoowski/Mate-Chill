import stripe
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from stripe.error import SignatureVerificationError

from mate import settings
from mate.settings import FRONTEND_CHECKOUT_SUCCESS_URL, FRONTEND_CHECKOUT_FAILED_URL
from orders.models import Order
from payments.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY
webhook_secret = settings.STRIPE_WEBHOOK_SECRET


class CreateCheckoutSession(APIView):
    def post(self, request):
        print(request.data)
        data = request.data['data']
        shipping_cost = request.data['shippingCost']
        order_id = request.data['orderId']
        try:
            line_items = []
            shipping_options = [
                {
                  "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": round(float(shipping_cost) * 100), "currency": "pln"},
                    "display_name": "Dostawa"
                  },
                }
              ]
            print(data)
            for element in data:
                line_items.append(
                    {
                        'price_data': {
                            'currency': 'pln',
                            'product_data': {
                                'name': element['name'],
                            },
                            'unit_amount': round(float(element['price']) * 100.00)
                        },
                        'quantity': round(int(element['count']))
                    }
                )
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                shipping_options=shipping_options,
                customer_email=request.user.email,
                locale='pl',
                mode='payment',
                metadata={
                    'orderId': order_id
                },
                success_url=f"{FRONTEND_CHECKOUT_SUCCESS_URL}/{order_id}",
                cancel_url=f"{FRONTEND_CHECKOUT_FAILED_URL}/{order_id}",
            )
            return Response({'session': checkout_session}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return e


@method_decorator(csrf_exempt, name='dispatch')
class WebHook(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        endpoint_secret = webhook_secret
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle the checkout.session.completed event
        if event['type'] == 'checkout.session.completed':
            order_id = event['data']['object']['metadata']['orderId']
            order = Order.objects.get(pk=order_id)
            order.status = 'opłacone'
            order.save()
            Payment.objects.create(user=request.user, order=order, amount=order.summary_cost)
        return HttpResponse(status=200)
