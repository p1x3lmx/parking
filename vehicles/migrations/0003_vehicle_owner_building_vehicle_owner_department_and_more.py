# Generated by Django 5.0.6 on 2024-07-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0002_vehicle_vehicle_manufacturer"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="owner_building",
            field=models.CharField(default="", max_length=254),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="owner_department",
            field=models.CharField(default="", max_length=254),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="owner_employee_id",
            field=models.CharField(default="", max_length=6),
        ),
    ]
