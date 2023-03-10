import os

from django.db import models
from django.utils.text import slugify


def upload_location(instance, filename):
    return os.path.join(
        "products", "%s" % instance.name, filename)


def upload_location_gallery(instance, filename):
    return os.path.join(
        "products", "%s" % instance.product.name, filename)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def save(
            self, *args, **kwargs
    ):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Manufacturer, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='subcategories', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def __str__(self):
        if self.parent is not None:
            return f'{self.parent.name} | wariant: {self.name}'
        return self.name

    def get_absolute_url(self):
        return 'categories/%s/' % self.slug

    def save(
            self, *args, **kwargs
    ):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default='', related_name='products',
                                     null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    num_available = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True, null=True)
    main_image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    grams_weight = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=25, blank=True, null=True)
    cm_length = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        if self.parent is not None:
            return f'{self.parent.name} | wariant: {self.name}'
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.country = self.parent.country
            self.manufacturer = self.parent.manufacturer
            self.description = self.parent.description
            if not self.main_image:
                self.main_image = self.parent.main_image
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/products/%s/' % self.slug


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location_gallery, blank=True, null=True)

    def __str__(self):
        return self.image.name
