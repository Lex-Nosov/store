from .models import Category
from app_shopping_cart.shopping_cart import Cart


def get_categories(request):
    return {'categories': Category.objects.all()
            }


def get_products_in_cart(request):
    return {'cart': [ids['product'].name for ids in Cart(request)],
            }
