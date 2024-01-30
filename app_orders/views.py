from typing import Any
from django.db.models.query import QuerySet
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .forms import FormOrder
from .models import Order, OrderItems
from app_shopping_cart.shopping_cart import Cart
from app_store.models import Product


class MainView(ListView):
    model = Order
    template_name = 'order_temp/order/orders.html'


class CreateOrder(CreateView):
    model = Order
    template_name = 'order_temp/order/create_order.html'
    form_class = FormOrder

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = FormOrder(request.POST)
        
        if form.is_valid():
            products = form.save()
            for item in cart:
                OrderItems.objects.create(
                    order=products,
                    items=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
                product = Product.objects.get(id=item['product'].id)
                Product.objects.filter(id=item['product'].id).update(stock=product.stock - item['quantity'])
            cart.clear()
        else:
            return render(request, self.template_name, context={'form': form})
        return redirect(reverse('orders'))


class DeleteOrder(DeleteView):
    model = Order
    template_name = 'order_temp/order/delete_order.html'
    success_url = '/'

