# CarRental
 ISD22 Challenge for renting cars.
 
This is a very basic project using Django that was created in context of the Information Systems Development course at the University of Liechtenstein.

# Get started

1. Clone the repository

````shell
git clone https://github.com/langekevin/CarRental.git
````

2. Get into the folder

````shell
cd CarRental
````

3. Install necessary packages
````shell
pip install -r requirements.txt 
````

4. Migrate database

````shell
python manage.py migrate
````

5. Create superuser
````shell
python manage.py createsuperuser
Username (leave blank to use 'kevinlange'): <USERNAME>
Email address: <EMAIL_ADDRESS>
Password: <PASSWORD>
Password (again): <PASSWORD>
Superuser created successfully.
````

6. Start the server

````shell
python manage.py runserver
````
