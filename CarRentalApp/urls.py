from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customers/new', views.new_customer, name='newcustomer'),
    path('customers/<int:customerid>/', views.edit_customer, name='editcustomer'),
    path('customers/<int:customerid>/delete', views.delete_customer, name='deletecustomer'),
    path('cars/', views.cars, name='cars'),
    path('cars/new', views.new_car, name='new-car'),
    path('cars/<int:car_id>/', views.edit_car, name='edit-car'),
    path('cars/<int:car_id>/delete', views.delete_car, name='delete-car'),
    path('rentcar/', views.rent_car, name='rentcar'),
    path('rentcar/new', views.new_car_rent, name='rentcar-new'),
    path('rentcar/<int:rental_id>/', views.rental_edit, name='rental-details'),
    path('rentcar/<int:rental_id>/return', views.return_car, name='return-car'),
    path('rentcar/<int:rental_id>/expand', views.expand_renting_duration, name='expand-renting-duration')
]
