from django.db import models
import datetime as dt


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
    rental_status = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.model} - {self.licence_plate}"


class Rental(models.Model):
    """
    Representation of a renting contract
    """
    due_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name='rental', on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, related_name='rental', on_delete=models.RESTRICT)

    def status(self) -> str:
        today = dt.date.today()
        if self.due_date > today:
            diff = self.due_date - today
            print(diff.days)
            return f'{diff.days} day{"" if diff.days == 1 else "s"} left'
        if self.due_date == today:
            return 'Due today'
        if self.due_date < today:
            diff = today - self.due_date
            return f'Due since {diff.days} days'
