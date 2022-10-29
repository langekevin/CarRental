# CarRental
 ISD22 Challenge for renting cars.
 
This is a very basic project using Django that was created in context of the Information Systems Development course at the University of Liechtenstein.


# Django Setup

1. Create Django project
````shell
django-admin startproject <PROJECT_NAME>
````
2. Enter project
````shell
cd <PROJECT_NAME>
````
3. Migrate django
````shell
 python manage.py migrate
````
4. Create superuser
````shell
python manage.py createsuperuser
Username (leave blank to use 'kevinlange'): <USERNAME>
Email address: <EMAIL_ADDRESS>
Password: <PASSWORD>
Password (again): <PASSWORD>
Superuser created successfully.
````
5. Start server
````shell
python manage.py runserver 
````
6. Create an app
````shell
python manage.py startapp <SITE_NAME>
````
