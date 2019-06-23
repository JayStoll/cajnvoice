from django.db import models


class Vehicles(models.Model):
    serial_num = models.TextField()

class Clients(models.Model):
    # set these to proper model data structure
    client_f_name = models.TextField()
    client_l_name = models.TextField()
    vehicles = Vehicles()