from django.contrib import admin
from .models import Vehicle, Clients, Parts, Vehicle_Work

admin.site.register(Vehicle)
admin.site.register(Clients)
admin.site.register(Parts)
admin.site.register(Vehicle_Work)
