from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Customer, Car
from .forms import NewCustomerForm, CarForm


def index(request):
    """
    Simple Start screen for car renting application
    """
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
        if Customer.objects.filter(id=customerid).count() == 0:
            return redirect(customers)
        customer_data = Customer.objects.get(id=customerid)
        form = NewCustomerForm(instance=customer_data)
        return render(request, "customers/customeredit.html", {'customer': customer_data, 'form': form})


def delete_customer(request, customerid: int):
    """
    Deletes a customer from the database
    """
    customer = Customer.objects.get(id=customerid)
    customer.delete()
    return redirect(customers)


def cars(request):
    """
    Gets all the cars from the database and gives the possibility
    to create a new car.
    """
    form = CarForm(request.POST)
    car_data = Car.objects.all().order_by('model')
    return render(request, 'cars/cars.html', {'cars': car_data, 'form': form})


def new_car(request):
    """
    Creates a new car in the database if the formdata is valid
    """
    if request.method == 'POST' and request.POST:
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            car_data = Car.objects.all().order_by('model')
            return render(request, 'cars/cars.html', {'cars': car_data, 'form': form})
    return redirect(cars)


def edit_car(request, car_id):
    """
    Updates the data of a car
    """
    if request.method == "POST" and request.POST:
        form = CarForm(request.POST)
        car = Car.objects.filter(id=car_id).first()
        if car.licence_plate != form.data.get('licence_plate'):
            # User updated the licence plate of the car
            # Check if the new licence plate is already used
            is_used = Car.objects.filter(licence_plate=form.data.get('licence_plate')).count() > 0
            if is_used:
                return render(request, "cars/carsedit.html", {'car': car, 'form': form})
        car.licence_plate = form.data.get('licence_plate')
        car.save()
        return redirect(cars)

    if Car.objects.filter(id=car_id).count() == 0:
        return redirect(cars)
    car_data = Car.objects.get(id=car_id)
    form = CarForm(instance=car_data)
    return render(request, "cars/carsedit.html", {'car': car_data, 'form': form})


def delete_car(request, car_id: int):

    try:
        car = Car.objects.get(id=car_id)
        car.delete()
    except Exception as e:
        print(e)

    return redirect(cars)


def rent_car(request):

    return render(request, 'rentcar.html', {})
