from django import forms

class AddWorkDoneForm(forms.Form):
    last_service_date = forms.DateField(label="Date of last service (MM/DD/YYYY)") # see about changing the order of this
    last_service_hours = forms.IntegerField(label="Hours/KM since last service")
    work_done = forms.CharField(widget=forms.Textarea)

class AddPartForm(forms.Form):
    part_name = forms.CharField(label="Part Name")
    part_serial_num = forms.CharField(label="Serial Number")

class AddVehicleForm(forms.Form):
    vehicle_brand = forms.CharField(label='Vehicle Brand', max_length=25)
    vehicle_type = forms.CharField(label='Vehicle Type', max_length=25)

class AddClientForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email', required=False)
    address = forms.CharField(label='Mailing Address', max_length=50)
    postal_code = forms.CharField(label='Postal Code', max_length=7)
    city = forms.CharField(label='City', max_length=30)