from django.contrib import admin

from products.models import Category, Product, Manufacturer, ProductImage


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }

    class Media:
        js = ("add_model_admin.js",)


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
admin.site.register(ProductImage)
