from django.db import models


class Vehicle(models.Model):
    LICENSE_PLATE_MAX_LENGTH = 15
    EMPLOYEE_ID_MAX_LENGTH = 6

    license_plate = models.CharField(
        max_length=LICENSE_PLATE_MAX_LENGTH, unique=True)
    owner_employee_id = models.CharField(
        max_length=EMPLOYEE_ID_MAX_LENGTH, default="")
    owner_name = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=15)
    owner_email = models.EmailField(max_length=254)
    owner_department = models.CharField(max_length=254, default="")
    owner_building = models.CharField(max_length=254, default="")
    vehicle_manufacturer = models.CharField(max_length=100, default="")
    vehicle_model = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.license_plate} - {self.vehicle_model}"
