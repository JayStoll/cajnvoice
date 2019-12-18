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

    return redirect('cajn-client', id)

def UpdateClientById(id, vehicle_id):
    Clients.objects.get(pk = id).vehicles.add(vehicle_id)

# find a way to clean this code up
def ReturnClientInfoList():
    info = [Clients._meta.get_field('client_f_name'), Clients._meta.get_field('client_l_name'), Clients._meta.get_field('client_email'),
            Clients._meta.get_field('mailing_address'), Clients._meta.get_field('postal_code'), Clients._meta.get_field('city')]
    return info

@login_required
def EditClient(request, id):
    client = Clients.objects.get(pk = id)
    field_objects = ReturnClientInfoList()

    if request.method == 'POST':
        form = AddClientForm(request.POST)
    else: 
        # currently doesn't work, might have to hard code in html tags
        form = AddClientForm(initial={'first_name': getattr(client, field_objects[0].attname), 'last_name': getattr(client, field_objects[1].attname),
                                    'email': getattr(client, field_objects[2].attname), 'address': getattr(client, field_objects[3].attname),
                                    'postal_code': getattr(client, field_objects[4].attname), 'city': getattr(client, field_objects[5].attname)})

    page = render(request, 'site/clients-pages/edit-client-info.html', {'form': form})

    if form.is_valid():
        print("Valid")
        Clients.objects.filter(pk = id).update(client_f_name = form.cleaned_data["first_name"], client_l_name = form.cleaned_data["last_name"], 
                        client_email = form.cleaned_data["email"], mailing_address = form.cleaned_data["address"], 
                        postal_code = form.cleaned_data["postal_code"], city = form.cleaned_data["city"])

        return redirect('cajn-client', id)

    return page