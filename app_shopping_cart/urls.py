from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='detail_cart'),
    path('add/<int:product_id>', views.cart_add, name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='remove_cart'),
]
