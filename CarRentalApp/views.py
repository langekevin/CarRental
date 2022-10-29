import datetime as dt
from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from .models import Customer, Car, Rental
from .forms import NewCustomerForm, CarForm, RentalForm
from .validations import is_future_date


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

    try:
        customer_data = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return redirect(customers)

    form = NewCustomerForm(instance=customer_data)
    return render(request, "customers/customeredit.html", {'customer': customer_data, 'form': form})


def delete_customer(request, customerid: int):
    """
    Deletes a customer from the database
    """
    try:
        customer = Customer.objects.get(id=customerid)
        customer.delete()
    except Customer.DoesNotExist:
        pass

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

    try:
        car_data = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return redirect(cars)

    form = CarForm(instance=car_data)
    return render(request, "cars/carsedit.html", {'car': car_data, 'form': form})


def delete_car(request, car_id: int):
    """
    Function for deleting a car from the database.
    """
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
    except Car.DoesNotExist:
        pass

    return redirect(cars)


def rent_car(request, form=None):
    """
    Creates the overview page for the rented cars as well as the
    form for renting a car
    """
    if form is None:
        form = RentalForm(request.POST)
    rental_data = Rental.objects.all().order_by('due_date')
    available_cars = Car.objects.filter(rental_status=False)
    customer_data = Customer.objects.all()

    return render(
        request,
        'carrenting/carrenting.html',
        {
            'rentals': rental_data,
            'form': form,
            'available_cars': available_cars,
            'customers': customer_data
        }
    )


def new_car_rent(request):
    """
    Creates a new renting contract in the database
    """
    if request.method == 'POST' and request.POST:
        form = RentalForm(request.POST)
        if form.is_valid() and is_future_date(form.data.get('due_date')):
            car_id = form.data.get('car')
            car_instance = Car.objects.get(id=car_id)
            car_instance.rental_status = True
            car_instance.due_date = form.data.get('due_date')
            car_instance.save()

            form.save()
        else:
            rental_data = Rental.objects.all().order_by('due_date')
            available_cars = Car.objects.filter(rental_status=False)
            customer_data = Customer.objects.all()
            return render(
                request,
                'carrenting/carrenting.html',
                {
                    'rentals': rental_data,
                    'form': form,
                    'available_cars': available_cars,
                    'customers': customer_data
                }
            )
    return redirect(rent_car, )


def rental_edit(request, rental_id: int):
    """
    Gets the information for a single renting contract
    """
    try:
        rental_contract = Rental.objects.get(id=rental_id)
    except Rental.DoesNotExist:
        return redirect(rent_car)

    return render(request, 'carrenting/carrentingdetails.html', {'rental': rental_contract})


def return_car(request, rental_id: int):
    """
    When the customer returns the car, the renting contract will be deleted.
    """
    try:
        rental_contract = Rental.objects.get(id=rental_id)
    except Rental.DoesNotExist:
        return redirect(rent_car)

    car_id = rental_contract.car.id

    # Reset rental status in Car object
    car = Car.objects.get(id=car_id)
    car.rental_status = False
    car.due_date = None
    car.save()

    # Delete Rental contract
    rental_contract.delete()
    return redirect(rent_car)


def expand_renting_duration(request, rental_id: int):
    """
    Expands the renting duration by one month.
    """
    try:
        rental_contract = Rental.objects.get(id=rental_id)
    except Rental.DoesNotExist:
        return redirect(rent_car)

    rental_contract.due_date += relativedelta(months=+1)
    rental_contract.save()

    car_id = rental_contract.car.id
    car = Car.objects.get(id=car_id)
    car.due_date = rental_contract.due_date
    car.save()

    return redirect(rent_car)
