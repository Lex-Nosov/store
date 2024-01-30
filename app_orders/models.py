from django.db import models
from app_store.models import Product


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    second_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    paid_for = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.order_number


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)


    @property
    def __str__(self):
        return self.items
