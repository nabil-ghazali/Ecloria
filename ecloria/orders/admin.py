from django.contrib import admin
from orders.models import  Order, Cart


# Register the Order model so it appears in Django admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'ordered', 'created_at', 'updated_at')
    list_filter = ('ordered', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')
    
admin.site.register(Cart)