from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from mate.settings import EMAIL_HOST_USER
from payments.models import Payment


@receiver(post_save, sender=Payment)
def payment_create_handler(sender, instance, created, **kwargs):
    if created:
        mail_subject = f'Mate&Chill - płatność za zamówienie #{instance.pk}'
        message = render_to_string("payments/payment_create_email.html", {
            "payment": instance,
        })
        to_email = instance.user.email
        send_email = EmailMessage(from_email=EMAIL_HOST_USER, subject=mail_subject, body=message, to=[to_email])
        send_email.content_subtype = 'html'
        send_email.send()