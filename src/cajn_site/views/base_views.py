from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import Clients

def home(request):
    return render(request, 'site/home.html')

@login_required
def ManageClients(request):
    return render(request, 'site/clients-pages/manage-clients.html', {'all_clients': Clients.objects.all()})

##############################
#   This is will be moved to an invoice view .py file later!
##############################
@login_required
def CreateInvoice(request):
    return render(request, 'site/invoice_generation_pages/invoice.html')