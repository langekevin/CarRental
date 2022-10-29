from django.contrib import admin
from .models import Customer
from .models import Car
from .models import Rental


admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Rental)
