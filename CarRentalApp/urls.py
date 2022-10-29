from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('rentcar/', views.rent_car, name='rentcar'),
    path('customers/new', views.new_customer, name='newcustomer'),
    path('customers/<int:customerid>/', views.edit_customer, name='editcustomer'),
    path('customers/<int:customerid>/delete', views.delete_customer, name='deletecustomer'),
    path('cars/', views.cars, name='cars'),
    path('cars/new', views.new_car, name='new-car'),
    path('cars/<int:car_id>/', views.edit_car, name='edit-car'),
    path('cars/<int:car_id>/delete', views.delete_car, name='delete-car')
]
