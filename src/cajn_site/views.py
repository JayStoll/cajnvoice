from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Clients, Vehicle
from .forms import AddClientForm, AddVehicleForm

def home(request):
    return render(request, 'site/home.html')

@login_required
def ManageClients(request):
    all_clients = Clients.objects.all()
    return render(request, 'site/clients-pages/manage-clients.html', {'all_clients': all_clients})


######################### Client Pages ###########################

@login_required
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
        add_vehicle = request.POST["vehicles"]
        if Vehicle.objects.count() > 0 and add_vehicle != "null":
            AddClient_vehicle(form, add_vehicle)
        else:
            AddClient(form)
        # return back to the main home page
        return redirect('cajn-manage-clients')

    # default return
    return page

@login_required
def AddClient_vehicle(form, add_vehicle):
    new_client = AddClient(form)
    new_client.vehicles.add(add_vehicle)

@login_required
def AddClient(form):
    # get the cleaned data from the form and create a new object using said data
    new_client = Clients.objects.create(client_f_name = form.cleaned_data["first_name"], client_l_name = form.cleaned_data["last_name"], 
                                client_email = form.cleaned_data["email"], mailing_address = form.cleaned_data["address"], 
                                postal_code = form.cleaned_data["postal_code"], city = form.cleaned_data["city"])
    return new_client


@login_required
def ClientManagePage(request, client_id):
    client_info = Clients.objects.get(pk = client_id)
    return render(request, 'site/clients-pages/client-info.html', {'client_info': client_info})

@login_required
def DeleteClient(request, id):
    client_info = Clients.objects.get(pk = id)
    client_info.delete()
    return redirect('cajn-manage-clients')

@login_required
def EditClient(request, id):
    client = Clients.objects.get(pk = id)

    if request.method == 'POST':
        form = AddClientForm(request.POST)
    else:
        form = AddClientForm()
    
    page = render(request, 'site/clients-pages/edit-client-info.html', {'form': form})

    if form.is_valid():
        AddClient(form)
        return redirect('cajn-manage-clients')

    return page
    # print the form filling the client information into the fields
    # check if the add button was clicked
        # update the client info and redirect to the client page
    # check if the cancel button was clicked
        # just redirect to the client page


######################### Vehicle Pages ###########################

@login_required
def AddVehicleView(request):
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
    else:
        form = AddVehicleForm()

    page = render(request, 'site/add-info-pages/add-vehicle.html', {'form': form})

    if form.is_valid():
        Vehicle.objects.create(vehicle_brand = form.cleaned_data["vehicle_brand"], vehicle_type = request.POST["vehicle_type"])
        return redirect('cajn-manage-clients')

    return page
    
    