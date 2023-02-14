from django.contrib import admin

from products.models import Category, Product, Manufacturer


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
