from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Vehicle
from ..forms import AddVehicleForm

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