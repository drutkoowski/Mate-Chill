from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from mate.settings import EMAIL_HOST_USER
from orders.models import Order


@receiver(post_save, sender=Order)
def order_create_handler(sender, instance, created, **kwargs):
    if created:
        mail_subject = f'Mate&Chill - zamówienie #{instance.pk}'
        message = render_to_string("orders/order_create_email.html", {
            "order": instance,
        })
        to_email = instance.user.email
        send_email = EmailMessage(from_email=EMAIL_HOST_USER, subject=mail_subject, body=message, to=[to_email])
        send_email.content_subtype = 'html'
        send_email.send()