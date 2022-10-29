from django.forms import ModelForm
from django import forms
from .models import Customer, Car


class NewCustomerForm(ModelForm):
    """
    Form to add a new customer
    """
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'mail']


class CarForm(ModelForm):
    """
    Form to add a new car
    """
    class Meta:
        model = Car
        fields = ['model', 'licence_plate']
