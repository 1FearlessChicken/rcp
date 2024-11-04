from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from usermgt.views import login_required, alogin_required

@login_required
def view_complaints(request):
    # complaints = Complaints.objects.all()
    complaints = Complaints.objects.filter(owner=request.user)
    d=[]
    for c in complaints:
        org=Organization.objects.get(id=c.organization).organization_name
        s=Software.objects.get(id=c.software).software_name
        a={'organization':org, 'software':s, 'complaint':c.complaint, 'date':c.date, 
           'resolution':c.resolution, 'user':c.owner,'id':c.id}
        d.append(a)
    context = {
        'complaints' : d,    
    }
    return render(request, 'complaints.html', context)


@alogin_required
def aview_complaints(request):
    complaints = Complaints.objects.all()
    d=[]
    for c in complaints:
        org=Organization.objects.get(id=c.organization).organization_name
        s=Software.objects.get(id=c.software).software_name
        a={'organization':org, 'software':s, 'complaint':c.complaint, 'date':c.date, 
           'resolution':c.resolution,'id':c.id}
        d.append(a)
    context = {
        'complaints' : d,    
    }
    return render(request, 'admincomplaints.html', context)


@login_required
def add_complaint(request):
    if request.method == 'POST':
        
        form = complaintForm(request.POST)
        
        if form.is_valid():
            
            complaint = form.cleaned_data['complaint']
            date = form.cleaned_data['date']
            resolution = form.cleaned_data['resolution']
            organization = form.cleaned_data['organization']
            software = form.cleaned_data['software']
            c = Complaints(complaint=complaint, date=date, resolution=resolution,
                           organization=organization, software=software, owner=request.user)
            c.save()
            
            return redirect('/complaints/')
        else:
            print(form.errors)
            varerr1="Input all fields"
            return render(request,'addcomplaint.html', {'form':form,'varerr':varerr1})
    else:
        form = complaintForm
        return render(request,'addcomplaint.html', {'form':form})


@login_required
def edit_complaint(request, id):
    complaint = get_object_or_404(Complaints, pk=id)
    if request.method == 'POST':
        form = complaintForm(request.POST)
        if form.is_valid():
            organization = form.cleaned_data['organization']
            complaint = form.cleaned_data['complaint']
            software = form.cleaned_data['software']
            resolution = form.cleaned_data['resolution']

        Complaints.objects.filter(organization = organization, complaint = complaint, software = software, 
                              resolution = resolution).update(organization = organization, complaint = complaint,                                   
                             software = software, resolution = resolution)

        return redirect('/complaints/')
    else:
        form = complaintForm(initial={'organization':complaint.organization, 'resolution':complaint.resolution, 'complaint':complaint.complaint, 'software':complaint.software,
                                      'date':complaint.date})
        return render(request,'editcomplaint.html', {'form':form})


@alogin_required
def delete_complaint(request, id):
    complaint = Complaints.objects.get(pk=id)
    complaint.delete()
    
    return redirect('complaints')


@alogin_required
def add_software(request):
    
    softwares = Software.objects.all()
    d=[]
    for c in softwares:
        a={'software_name':c.software_name,'id':c.id}
        d.append(a)
        
    if request.method == 'POST':
        
        form = softwareForm(request.POST)
        
        if form.is_valid():
            
            software_name = form.cleaned_data['software_name']
            
            s = Software(software_name=software_name)
            s.save()
            return HttpResponseRedirect('/addsoftware/')
        else:
            print(form.errors)
            varerr1="Input all fields"
            return render(request,'addsoftware.html', {'form':form,'varerr':varerr1, 'softwares':d})
    else:
        form = softwareForm
        return render(request,'addsoftware.html', {'form':form, 'softwares':d})


@alogin_required
def edit_software(request, id):
    software = get_object_or_404(Software, pk=id)
    
    if request.method == 'POST':
        form = softwareForm(request.POST)
        
        if form.is_valid():
            
            software_name = form.cleaned_data['software_name']

        Complaints.objects.filter(software_name = software_name).update(software_name = software_name)

        return redirect('/addsoftware/')
    else:
        form = softwareForm(initial={'software_name':software.software_name})
        return render(request,'editsoftware.html', {'form':form})


@alogin_required
def delete_software(request):
    software = Software.objects.get(pk=id)
    software.delete()
    
    return redirect('softwares')


@alogin_required
def add_organization(request):
    
    organizations = Organization.objects.all()
    d=[]
    
    for c in organizations:
        a={'organization_name':c.organization_name, 'email':c.email, 'phone_number':c.phone_number,'id':c.id}
        d.append(a)
        
    if request.method == 'POST':
        
        form = organizationForm(request.POST)
        
        if form.is_valid():
            organization_name = form.cleaned_data['organization_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            
            s = Organization(organization_name=organization_name, email=email, phone_number=phone_number)
            s.save()
            return HttpResponseRedirect('/organizations/')
        else:
            print(form.errors)
            varerr1="Input all fields"
            return render(request,'organizations.html', {'form':form,'varerr':varerr1, 'organizations':d})
    else:
        form = organizationForm
        return render(request,'organizations.html', {'form':form, 'organizations':d})


@alogin_required
def edit_organization(request, id):
    organization = get_object_or_404(Organization, pk=id)
    
    if request.method == 'POST':
        form = organizationForm(request.POST)
        
        if form.is_valid():
            organization_name = form.cleaned_data['organization_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']

        Organization.objects.filter(organization_name=organization_name, email=email, phone_number=phone_number).update(organization_name=organization_name, email=email, phone_number=phone_number)

        return redirect('/organizations/')
    else:
        form = organizationForm(initial={'organization_name':organization.organization_name, 'email':organization.email, 'phone_number':organization.phone_number})
        return render(request,'editorganization.html',{'form':form})


@alogin_required
def delete_organization(request):
    organization = Organization.objects.get(pk=id)
    organization.delete()
    
    return redirect('organizations')



def stats1(request):
    pass



def stats2(request):
    pass