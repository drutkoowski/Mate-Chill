from django.contrib import admin

from orders.models import Order, OrderProduct


class OrderInlineAdmin(admin.TabularInline):
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInlineAdmin]
    readonly_fields = ('total_product_cost', 'shipping_cost', 'summary_cost',)


class OrderProductAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)


admin.site.register(Order)
admin.site.register(OrderProduct, OrderProductAdmin)
