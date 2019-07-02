from django.db import models

class Vehicle(models.Model):
    vehicle_type = models.TextField()

class Clients(models.Model):
    # set these to proper model data structure
    client_f_name = models.TextField()
    client_l_name = models.TextField()