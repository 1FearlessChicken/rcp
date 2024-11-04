from argparse import Action
from django import forms

status=(
    ('active','active'),
    ('inactive','inactive'),
)

    

class adminForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4)
    password = forms.CharField(label='Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    status = forms.ChoiceField(label='Status', choices=status)
    
    def __init__(self, *args, **kwargs):
        super(adminForm, self).__init__(*args, **kwargs)
        
        #Initialization of the form
        self.fields['username'].widget.attrs.update({'class':'form-control', 'id':'floatingInput', 'placeholder':'Username', 'type':'text'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        self.fields['status'].widget.attrs.update({'class':'form-control', 'placeholder':'status'})
        


class adminLogin(forms.Form):
    username = forms.CharField(label='Username', min_length=4)
    password = forms.CharField(label='Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    
    def __init__(self, *args, **kwargs):
        super(adminLogin, self).__init__(*args, **kwargs)
        
        #Initialization of the form
        self.fields['username'].widget.attrs.update({'class':'form-control', 'id':'floatingInput', 'placeholder':'Username', 'type':'text'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        
        

class userForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4)
    password = forms.CharField(label='Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    status = forms.ChoiceField(label='Status', choices=status)
    organization = forms.ChoiceField(label='Organization', choices=[])
    phone_number = forms.CharField(label='Phone Number')
    
    def __init__(self, *args, **kwargs):
        super(userForm, self).__init__(*args, **kwargs)
        
        # Fetch data from the database and set it as choices for organizations and software
        from complaints.models import Organization
        self.fields['organization'].choices = [(obj.id, obj.organization_name) for obj in Organization.objects.all()]

        # Initialization of the form
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        self.fields['status'].widget.attrs.update({'class':'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control'})
        self.fields['organization'].widget.attrs.update({'class':'form-control'})
        
        
        
class changepasswordForm(forms.Form):
    password = forms.CharField(label='Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    newpassword = forms.CharField(label='New Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    c_newpassword = forms.CharField(label='Confirm New Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    
    def __init__(self, *args, **kwargs):
        super(changepasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        self.fields['newpassword'].widget.attrs.update({'class':'form-control'})
        self.fields['c_newpassword'].widget.attrs.update({'class':'form-control'})
        
        
class edituserForm(forms.Form):
    status = forms.ChoiceField(label='Status', choices=status)
    
    def __init__(self, *args, **kwargs):
        super(edituserForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class':'form-control'})
    
        
    
class login(forms.Form):
    username = forms.CharField(label='Username', min_length=4)
    password = forms.CharField(label='Password', min_length=7, widget=forms.PasswordInput({"placeholder":"Password"}))
    
    def __init__(self, *args, **kwargs):
        super(login, self).__init__(*args, **kwargs)
        
        #Initialization of the form        self.fields['organization'].choices = [(obj.id, obj.organization_name) for obj in Organization.objects.all()]

        self.fields['username'].widget.attrs.update({'class':'form-control', 'id':'floatingInput', 'placeholder':'Username', 'type':'text'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})