from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'site/home.html')

def ManageClients(request):
    ############ ToDo ##################
    #  1. Get the client information and put into array
    #  2. print out the first and last name into clickable links/buttons
    #  3. when client is clicked display vehicles 
    return render(request, 'site/clients-pages/manage-clients.html')