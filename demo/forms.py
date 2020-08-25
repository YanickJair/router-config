from django import forms

from . import models

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['ip', 'hostname', 'client_name', 'address', 'technician_contact', 'router']