from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="cajn-site-home"),
    path('manage-clients/', views.ManageClients, name='cajn-manage-clients')
]