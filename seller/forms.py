from datetime import datetime
from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput

from .models import Supplier

def validate_checked(value):
    if not value:
        raise ValidationError("Required.")
    
class SupplierProfileForm(forms.ModelForm):
    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true and i accept the terms.',
        validators=[validate_checked]
    )
    class Meta:
        model = Supplier
        fields = (
                'company',
                'contact_name',
                'phone',
                'email',
                'website',
                'supplier_location',
                'license_number',
                'license_states',
                'contract_plan',
                'confirmation',
                )
        widgets = {
            'company': forms.TextInput(attrs={'autofocus': True}),
            'website': forms.TextInput(
                attrs = {'placeholder':'https://www.example.com'}
            ),
        }