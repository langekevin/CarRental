# Generated by Django 4.1.2 on 2022-10-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CarRentalApp", "0003_remove_car_customer_id_remove_car_due_date_rental"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
