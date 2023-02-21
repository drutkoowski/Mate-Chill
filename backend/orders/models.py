from django.db import models
from accounts.models import Account
from products.models import Product

ORDER_STATUS_CHOICES = (
    ('nieopłacone', 'nieopłacone'),
    ('opłacone', 'opłacone'),
    ('w dostawie', 'w dostawie'),
    ('zakończone', 'zakończone')
)


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='orders')
    total_product_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0.00)
    shipping_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=9.99)
    summary_cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    additional_address = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default='nieopłacone', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} / {self.id}"

    def save(
            self, *args, **kwargs
    ):
        if self.pk:
            if self.products.count() > 0:
                self.total_product_cost = self.products.all().aggregate(summary_price=models.Sum('price'))['summary_price']
            self.shipping_cost = 0 if self.total_product_cost >= 60 else 9.99
            self.summary_cost = round(float(self.total_product_cost) + self.shipping_cost, 2)
        super(Order, self).save(*args, **kwargs)


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    count = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.product} / order-{self.order.id}"

    def save(
            self, *args, **kwargs
    ):
        self.price = round(self.product.price * self.count, 2)
        super(OrderProduct, self).save(*args, **kwargs)
