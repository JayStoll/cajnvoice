from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Vehicle, Clients, Vehicle_Work
from ..forms import AddVehicleForm, AddWorkDoneForm

@login_required
def AddVehicleView(request):
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
    else:
        form = AddVehicleForm()

    data_type = "Vehicle"
    page = render(request, 'site/add-info-pages/add-info-by-type.html', {'form': form, 'type':data_type})

    if form.is_valid():
        Vehicle.objects.create(vehicle_brand = form.cleaned_data["vehicle_brand"], vehicle_type = request.POST["vehicle_type"])
        return redirect('cajn-manage-clients')

    return page

@login_required
def VehicleInfoPage(request, client_id, vehicle_id):
    client = Clients.objects.get(pk = client_id)
    vehicle = Vehicle.objects.get(pk = vehicle_id)

    try:
        # get the work that has been done on the vehicle owned by the client
        work_done = Vehicle_Work.objects.get(client_id = client_id, vehicle_id=vehicle_id)
    except Vehicle_Work.DoesNotExist:
        work_done = "null"

    if request.method == 'POST':
        form = AddWorkDoneForm(request.POST)
    else:
        form = AddWorkDoneForm()

    return render(request, 'site/clients-pages/vehicle-info-page.html', {'client_info': client, "vehicle_info": vehicle, 'work':work_done})

@login_required
def AddWorkDone(request, client_id, vehicle_id):
    return redirect('cajn-manage-clients')