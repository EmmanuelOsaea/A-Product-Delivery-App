from django.contrib import admin
from  .models import Order, OrderItem # This import models

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'order_date', 'total_price')
    list_filter = ('status', 'order_date')
    search_fields = ('client_first_name', 'client_last_name', 'id')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity', 'price_per_item')
    search_field = ('product_name',)
