from django.urls import path
from .views import base_views as base, client_views as client, vehicle_views as vehicle

urlpatterns = [
    # visible page routes
    path('', base.home, name="cajn-site-home"),
    path('manage-clients/', base.ManageClients, name='cajn-manage-clients'),
    path('add-client/', client.AddClientView, name='cajn-add-client'),
    path('client-info/<int:client_id>', client.ClientManagePage, name='cajn-client'),
    path('add-vehicle/', vehicle.AddVehicleView, name='cajn-add-vehicle'),
    path('client-vehicle/<int:id>', client.AddVehicleClient_FormRequest),

    # add info to db routes
    path('DeleteClient/<int:id>', client.DeleteClient),
    #path('EditClient/<int:id>', views.EditClient),
    path('AddVehicleClient/<int:id>', client.AddVehicleToClient),
]