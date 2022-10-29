from django.forms import ModelForm
from django import forms
from .models import Customer, Car, Rental


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


class RentalForm(ModelForm):

    class Meta:
        model = Rental
        fields = ['due_date', 'customer', 'car']
