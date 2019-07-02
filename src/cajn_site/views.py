from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Clients

def home(request):
    return render(request, 'site/home.html')

def ManageClients(request):
    all_clients = Clients.objects.all()
    return render(request, 'site/clients-pages/manage-clients.html', {'all_clients': all_clients})


######################### Client Pages ###########################

def AddClientView(request):
    return render(request, 'site/add-info-pages/add-client.html')

def AddClient(request):
    new_item = Clients(client_f_name = request.POST["f_name"], client_l_name = request.POST["l_name"])
    new_item.save()
    return redirect('cajn-manage-clients')

def ClientManagePage(request, client_id):
    client_info = Clients.objects.get(pk = client_id)
    return render(request, 'site/clients-pages/client-info.html', {'client_info': client_info})

def DeleteClient(request, id):
    client_info = Clients.objects.get(pk = id)
    client_info.delete()
    return redirect('cajn-manage-clients')