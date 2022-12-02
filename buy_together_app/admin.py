from django.contrib import admin
from .models import supplierProduct, Product, Supplier


class supplierProductAdmin(admin.ModelAdmin):
    list_display = ('suppler_product_id', 'qr_code', 'user_name', 'price', 'quantity')


admin.site.register(supplierProduct, supplierProductAdmin)
admin.site.register(Product)
admin.site.register(Supplier)
