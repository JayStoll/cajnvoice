from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Clients, Vehicle
from .forms import AddClientForm

def home(request):
    return render(request, 'site/home.html')

def ManageClients(request):
    all_clients = Clients.objects.all()
    return render(request, 'site/clients-pages/manage-clients.html', {'all_clients': all_clients})


######################### Client Pages ###########################

def AddClientView(request):
    # figure if we should be using POST method
    if request.method == 'POST':
        form = AddClientForm(request.POST)
    else:
        form = AddClientForm()

    vehicles = Vehicle.objects.all()
    # render the page to the browser passing in vehcile information and the form needed
    page = render(request, 'site/add-info-pages/add-client.html', {'vehicle_list': vehicles, 'form': form})

    if form.is_valid():
        add_vehicle = "null"#= request.POST["vehicles"]
        AddClient(form, add_vehicle)
        # return back to the main home page
        return redirect('cajn-manage-clients')

    # default return
    return page

def AddClient(form, add_vehicle):
    # get the cleaned data from the form and create a new object using said data
    new_client = Clients.objects.create(client_f_name = form.cleaned_data["first_name"], client_l_name = form.cleaned_data["last_name"], 
                                        client_email = form.cleaned_data["email"], mailing_address = form.cleaned_data["address"], 
                                        postal_code = form.cleaned_data["postal_code"], city = form.cleaned_data["city"])

    #new_client.vehicles.add(add_vehicle)

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