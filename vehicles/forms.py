from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'owner_employee_id', 'owner_name',
                  'owner_contact', 'owner_email', 'owner_department', 'owner_building',
                  'vehicle_manufacturer', 'vehicle_model',
                  'vehicle_color']

        widgets = {
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'owner_department': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_building': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_model': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_color': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_license_plate(self):
        return self.cleaned_data['license_plate'].upper()

    def clean_owner_name(self):
        return self.cleaned_data['owner_name'].title()
