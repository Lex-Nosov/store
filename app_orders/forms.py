from django import forms
from .models import Order


class FormOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control border"}),
            "second_name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "address": forms.TextInput(attrs={"class": "form-control border"})
        }

