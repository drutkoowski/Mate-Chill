import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mate import settings
from mate.settings import FRONTEND_CHECKOUT_SUCCESS_URL, FRONTEND_CHECKOUT_FAILED_URL

stripe.api_key = settings.STRIPE_SECRET_KEY
webhook_secret = settings.STRIPE_WEBHOOK_SECRET


class CreateCheckoutSession(APIView):
    def post(self, request):
        dataDict = dict(request.data)
        price = dataDict['price']
        product_name = dataDict['product_name']
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'pln',
                        'product_data': {
                            'name': product_name,
                        },
                        'unit_amount': price * 100
                    },
                    'quantity': 1
                }],
                mode='payment',
                success_url=FRONTEND_CHECKOUT_SUCCESS_URL,
                cancel_url=FRONTEND_CHECKOUT_FAILED_URL,
            )
            return Response({'session': checkout_session})
        except Exception as e:
            print(e)
            return e


class WebHook(APIView):
    def post(self, request):
        event = None
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ValueError as err:
            # Invalid payload
            raise err
        except stripe.error.SignatureVerificationError as err:
            # Invalid signature
            raise err

        # Handle the event
        if event.type == 'payment_intent.succeeded':
            payment_intent = event.data.object
            print("--------payment_intent ---------->", payment_intent)
        elif event.type == 'payment_method.attached':
            payment_method = event.data.object
            print("--------payment_method ---------->", payment_method)
        # ... handle other event types
        else:
            print('Unhandled event type {}'.format(event.type))

        return JsonResponse(success=True, safe=False)
