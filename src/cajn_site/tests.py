from django.test import TestCase
from cajn_site.models import Clients

# Create your tests here.
class CreateClientTest(TestCase):
    def setUp(self):
        Clients.objects.create(client_f_name = "Jayden", client_l_name = "Stoll", 
                                client_email = "jstoll11@gmail.com", mailing_address = "B12-175 Columbia Blvd W", 
                                postal_code = "T1K 4B7", city = "Lethbridge")

    def test_first_name(self):
        jayden = Clients.objects.get(client_f_name = "Jayden")
        self.assertEqual(jayden.First_Name(), "Jayden")
    