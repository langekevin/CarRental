from django.forms import ModelForm
from django import forms
from .models import Customer


class NewCustomerForm(ModelForm):
    """
    Form to add a new customer
    """
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'mail']
