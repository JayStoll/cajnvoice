from django.urls import path
from . import views

urlpatterns = [
    # visible page routes
    path('', views.home, name="cajn-site-home"),
    path('manage-clients/', views.ManageClients, name='cajn-manage-clients'),
    path('add-client/', views.AddClientView, name='cajn-add-client'),
    path('client-info/<int:client_id>', views.ClientManagePage, name='cajn-client'),
    path('add-vehicle/', views.AddVehicleView, name='cajn-add-vehicle'),

    # add info to db routes
    path('DeleteClient/<int:id>', views.DeleteClient),
    path('AddNewVehicle/', views.AddVehicle),
]