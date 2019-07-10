from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Clients, Vehicle

def home(request):
    return render(request, 'site/home.html')

def ManageClients(request):
    all_clients = Clients.objects.all()
    return render(request, 'site/clients-pages/manage-clients.html', {'all_clients': all_clients})


######################### Client Pages ###########################

def AddClientView(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'site/add-info-pages/add-client.html', {'vehicle_list': vehicles})

def AddClient(request):
    new_client = Clients(client_f_name = request.POST["f_name"], client_l_name = request.POST["l_name"], client_email = request.POST["email"],
                         mailing_address = request.POST["add"], postal_code = request.POST["post_code"], city = request.POST["city"])
    new_client.save()
    return redirect('cajn-manage-clients')

def ClientManagePage(request, client_id):
    client_info = Clients.objects.get(pk = client_id)
    return render(request, 'site/clients-pages/client-info.html', {'client_info': client_info})

def DeleteClient(request, id):
    client_info = Clients.objects.get(pk = id)
    client_info.delete()
    return redirect('cajn-manage-clients')

######################### Vehicle Pages ###########################

def AddVehicleView(request):
    return render(request, 'site/add-info-pages/add-vehicle.html')

def AddVehicle(request):
    new_vehicle = Vehicle(vehicle_brand = request.POST["brand"], vehicle_type = request.POST["model"])
    new_vehicle.save()
    return redirect('cajn-manage-clients')