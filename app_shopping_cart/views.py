from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from app_store.models import Product
from .shopping_cart import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(cart_detail)


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_temp/cart/cart_detail.html', {'cart': cart})
