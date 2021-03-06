from django.db import models

class Parts(models.Model):
    part_name = models.TextField(blank=False)
    part_serial = models.TextField(blank=False)


class Vehicle(models.Model):
    vehicle_brand = models.TextField(blank=False)
    vehicle_type = models.TextField(blank=False)


class Clients(models.Model):
    client_f_name = models.TextField(max_length=20, blank=False)
    client_l_name = models.TextField(max_length=20, blank=False)
    client_email = models.TextField(blank=True)
    mailing_address = models.TextField(blank=False)
    postal_code = models.TextField(max_length=7, blank=False) # ADA DAD format required, 7 char max (includes space) 
    city = models.TextField(max_length=25, blank=False)
    vehicles = models.ManyToManyField(Vehicle, blank=True, unique=False)


class Vehicle_Work(models.Model):
    work_done = models.TextField(blank=True)
    last_service_date = models.TimeField(blank=True)
    last_service_hours = models.PositiveIntegerField(blank=False)
    parts_id = models.ManyToManyField(Parts, blank=True, unique=False) # allow a list of parts to be added
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)

