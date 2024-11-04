from argparse import Action
from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class complaintForm(forms.Form):
    complaint = forms.CharField(label='Complaint', widget=forms.TextInput({ "placeholder": "Complaint"}))
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type':'date'}))
    resolution = forms.CharField(label='Resolution')
    organization = forms.ChoiceField(label='Organization', choices=[])
    software = forms.ChoiceField(label='Software', choices=[])
    
    def __init__(self, *args, **kwargs):
        super(complaintForm, self).__init__(*args, **kwargs)
        # Fetch data from the database and set it as choices for organizations and software
        self.fields['organization'].choices = [(obj.id, obj.organization_name) for obj in Organization.objects.all()]
        self.fields['software'].choices = [(obj.id, obj.software_name) for obj in Software.objects.all()]
        
        # Initialization of the form
        self.fields['date'].widget.attrs.update({'class':'form-control'})
        self.fields['resolution'].widget.attrs.update({'class':'form-control'})
        self.fields['complaint'].widget.attrs.update({'class':'form-control'})
        self.fields['software'].widget.attrs.update({'class':'form-control'})
        self.fields['organization'].widget.attrs.update({'class':'form-control'})
        
        

class softwareForm(forms.Form):
    software_name = forms.CharField(label='Software Name')
    
    def __init__(self, *args, **kwargs):
        super(softwareForm, self).__init__(*args, **kwargs)
        self.fields['software_name'].widget.attrs.update({'class':'form-control'})


class organizationForm(forms.Form):
    organization_name = forms.CharField(label='Organization Name')
    email = forms.EmailField(label='Email')
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        label="Phone Number",
        region="NG"
    )
    
    def __init__(self, *args, **kwargs):
        super(organizationForm, self).__init__(*args, **kwargs)
        self.fields['organization_name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})