from django.forms import ModelForm
from app_store.models import Product
from app_orders.models import Order


class FormProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class FormOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
