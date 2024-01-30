from django.contrib import admin
from .models import Order, OrderItems


class OrderItem(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['items']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name', 'second_name', 'email', 'address', 'created', 'updated']
    list_editable = ['first_name', 'second_name', 'email', 'address']
    search_fields = ['order_number', 'first_name', 'second_name', 'email', 'address']
    inlines = [OrderItem]
