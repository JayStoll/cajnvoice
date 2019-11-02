from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Parts
from ..forms import AddPartForm

@login_required
def AddPartView(request):
    if request.method == 'POST':
        form = AddPartForm(request.POST)
    else:
        form = AddPartForm()

    data_type = "Part"
    page = render(request, 'site/add-info-pages/add-info-by-type.html', {'form': form, 'type':data_type})

    if form.is_valid():
        Parts.objects.create(part_name = form.cleaned_data["part_name"], part_serial = request.POST["part_serial_num"])
        return redirect('cajn-manage-clients')

    return page