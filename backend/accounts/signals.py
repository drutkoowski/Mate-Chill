from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from accounts.models import Account
from mate.settings import EMAIL_HOST_USER,FRONTEND_CHECKOUT_SUCCESS_URL


@receiver(post_save, sender=Account)
def account_create_handler(sender, instance, created, **kwargs):
    if created:
        mail_subject = 'Mate&Chill - rejestracja konta'
        message = render_to_string("accounts/account_create_email.html", {
            "user": instance,
            "status_link": f'{FRONTEND_CHECKOUT_SUCCESS_URL}/{instance.pk}'
        })
        to_email = instance.email
        send_email = EmailMessage(from_email=EMAIL_HOST_USER, subject=mail_subject, body=message, to=[to_email])
        send_email.content_subtype = 'html'
        send_email.send()

