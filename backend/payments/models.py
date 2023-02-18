from django.db import models
from accounts.models import Account
from orders.models import Order


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='payments')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='payments')
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} / {self.order}"
