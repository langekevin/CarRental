from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('customers/', views.customers, name='customers'),
    path('rentcar/', views.rent_car, name='rentcar'),
    path('customers/new', views.new_customer, name='newcustomer'),
    path('customers/<int:customerid>/', views.edit_customer, name='editcustomer'),
    path('customers/<int:customerid>/delete', views.delete_customer, name='deletecustomer'),
]
