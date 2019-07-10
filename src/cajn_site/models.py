from django.db import models

class Vehicle(models.Model):
    vehicle_brand = models.TextField()
    vehicle_type = models.TextField()

class Vehicle_Work(models.Model):
    work_done = models.TextField(blank=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class Clients(models.Model):
    client_f_name = models.TextField(max_length=20, blank=False)
    client_l_name = models.TextField(max_length=20, blank=False)
    client_email = models.TextField(blank=True)
    mailing_address = models.TextField(blank=False)
    postal_code = models.TextField(max_length=7, blank=False) # ADA DAD format required, 7 char max (includes space) 
    city = models.TextField(max_length=25, blank=False)
    vehicle_id = models.ManyToManyField(Vehicle)