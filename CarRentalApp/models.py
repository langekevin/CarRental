from django.db import models


class Customer(models.Model):
    """
    Representation of a customer
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mail}"

class Car(models.Model):
    """
    Representation of a car
    """
    model = models.CharField(max_length=100)
    licence_plate = models.CharField(max_length=20)
    rental_status = models.BooleanField()
    due_date = models.DateField()
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_DEFAULT, default=0)

    def __str__(self):
        return f"{self.model} - {self.licence_plate} - {'Rented' if self.rental_status else 'Available'}"
