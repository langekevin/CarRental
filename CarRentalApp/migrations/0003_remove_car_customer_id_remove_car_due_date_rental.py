# Generated by Django 4.1.2 on 2022-10-29 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("CarRentalApp", "0002_alter_car_customer_id_alter_car_due_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="car", name="customer_id",),
        migrations.RemoveField(model_name="car", name="due_date",),
        migrations.CreateModel(
            name="Rental",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="rental",
                        to="CarRentalApp.car",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="rental",
                        to="CarRentalApp.customer",
                    ),
                ),
            ],
        ),
    ]