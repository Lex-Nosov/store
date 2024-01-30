from django.urls import path
from app_store.views import ProductView, MainView, ProductDetail

# from app_shopping_cart.views import OrderView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', MainView.as_view(), name='main'),
]
