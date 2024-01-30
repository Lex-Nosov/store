from django.urls import path
from app_orders.views import MainView, CreateOrder, DeleteOrder

urlpatterns = [
    path('', MainView.as_view(), name='orders'),
    path('create/', CreateOrder.as_view(), name='create_order'),
    path('delete/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
]
