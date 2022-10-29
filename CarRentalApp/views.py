from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Customer
from .forms import NewCustomerForm


def index(request):
    return render(request, 'index.html', {})


def customers(request):
    """
    Gets all the customers from the database and gives the possibility
    to create a user.
    """
    form = NewCustomerForm(request.POST)
    customer_data = Customer.objects.all().order_by('last_name')
    return render(request, 'customers/customers.html', {'customers': customer_data, 'form': form})


def new_customer(request):
    """
    Creates a new customer in the database if the formdata is valid
    """
    if request.method == 'POST' and request.POST:
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            customer_data = Customer.objects.all().order_by('last_name')
            return render(request, 'customers/customers.html', {'customers': customer_data, 'form': form})
    return redirect(customers)


def edit_customer(request, customerid: int):
    """
    Dependend on the request method, the page for updating a customer
    gets loaded or the customer gets updated.
    """
    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        customer = Customer.objects.filter(id=customerid).first()
        if customer.mail != form.data.get('mail'):
            # User updated the mail of the customer
            # Check if the new mail is already used
            is_used = Customer.objects.filter(mail=form.data.get('mail')).count() > 0
            if is_used:
                return render(request, "customers/customeredit.html", {'customer': customer, 'form': form})
        customer.first_name = form.data.get('first_name')
        customer.last_name = form.data.get('last_name')
        customer.mail = form.data.get('mail')
        customer.save()
        return redirect(customers)
    else:
        customer_data = Customer.objects.filter(id=customerid).first()
        form = NewCustomerForm(instance=customer_data)
        return render(request, "customers/customeredit.html", {'customer': customer_data, 'form': form})


def delete_customer(request, customerid: int):
    """
    Deletes a customer from the database
    """
    customer = Customer.objects.get(id=customerid)
    customer.delete()
    return redirect(customers)


def rent_car(request):
    return render(request, 'rentcar.html', {})


def cars(request):
    return render(request, 'cars.html', {})
