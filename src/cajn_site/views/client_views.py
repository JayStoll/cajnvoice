from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import Clients, Vehicle, Parts, Vehicle_Work
from ..forms import AddClientForm, AddWorkDoneForm

@login_required
def AddClientView(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
    else:
        form = AddClientForm()

    # render the page to the browser passing in vehcile information and the form needed
    page = render(request, 'site/add-info-pages/add-client.html', {'vehicle_list': Vehicle.objects.all(), 'form': form})
    if form.is_valid():
        if Vehicle.objects.count() > 0:
            add_vehicle = request.POST["vehicles"]
            if add_vehicle != "null":
                AddClient_vehicle(form, add_vehicle)
                return redirect('cajn-manage-clients')

        AddClient(form)
        # return back to the main home page
        return redirect('cajn-manage-clients')

    # default return
    return page

def AddClient_vehicle(form, add_vehicle):
    new_client = AddClient(form)
    new_client.vehicles.add(add_vehicle)

def AddClient(form):
    # get the cleaned data from the form and create a new object using said data
    new_client = Clients.objects.create(client_f_name = form.cleaned_data["first_name"], client_l_name = form.cleaned_data["last_name"], 
                                client_email = form.cleaned_data["email"], mailing_address = form.cleaned_data["address"], 
                                postal_code = form.cleaned_data["postal_code"], city = form.cleaned_data["city"])
    return new_client


@login_required
def ClientManagePage(request, client_id):
    return render(request, 'site/clients-pages/client-info.html', {'client_info': Clients.objects.get(pk = client_id)})

@login_required
def DeleteClient(request, id):
    client_info = Clients.objects.get(pk = id)
    client_info.delete()
    return redirect('cajn-manage-clients')


@login_required
def AddVehicleToClient(request, id):
    return render(request, 'site/clients-pages/add-vehicle-to-client.html', {'vehicle_list': Vehicle.objects.all(), 'client_info': Clients.objects.get(pk = id)})

def AddVehicleClient_FormRequest(request, id):
    vehicle_id = request.POST['vehicles']

    if vehicle_id != "null":
        UpdateClientById(id, vehicle_id)

    return redirect('cajn-manage-clients')

def UpdateClientById(id, vehicle_id):
    Clients.objects.get(pk = id).vehicles.add(vehicle_id)

@login_required
def CreateWorkDoneForm(request, client_id, vehicle_id):
    client = Clients.objects.get(pk = client_id)
    vehicle = Vehicle.objects.get(pk = vehicle_id)
    work_done = get_object_or_404(Vehicle_Work, client_id = client_id, vehicle_id = vehicle_id)

    if request.method == 'POST':
        form = AddWorkDoneForm(request.POST)
    else:
        form = AddWorkDoneForm()

    page = render(request, 'site/clients-pages/add-work-done.html', {'client_info': client, "vehicle_info": vehicle})

    return page

