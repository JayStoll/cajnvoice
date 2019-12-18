from django.urls import path
from .views import base_views as base, client_views as client, vehicle_views as vehicle, part_views as part

urlpatterns = [
    # visible page routes
    path(r'', base.home, name="cajn-site-home"),
    path(r'manage-clients/', base.ManageClients, name='cajn-manage-clients'),
    path(r'add-client/', client.AddClientView, name='cajn-add-client'),
    path(r'client-info/<int:client_id>', client.ClientManagePage, name='cajn-client'),
    path(r'add-vehicle/', vehicle.AddVehicleView, name='cajn-add-vehicle'),
    path(r'add-part/', part.AddPartView, name='cajn-add-part'),
    path(r'client-vehicle/<int:id>', client.AddVehicleClient_FormRequest),
    path(r'vehicle-info/<int:client_id>/<int:vehicle_id>', vehicle.VehicleInfoPage),
    path(r'work-done/<int:client_id>/<int:vehicle_id>', vehicle.AddWorkDone, name='cajn-work-done'),
    
    # This one will need to be updated when invoice generation is under development
    path(r'create-invoice/', base.CreateInvoice, name="cajn-site-create-invoice"),

    # add info to db routes
    path(r'DeleteClient/<int:id>', client.DeleteClient),
    path(r'EditClient/<int:id>', client.EditClient),
    path(r'AddVehicleClient/<int:id>', client.AddVehicleToClient),
]