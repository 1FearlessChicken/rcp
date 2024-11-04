from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from functools import wraps
from .forms import *
from .models import *

#Decorators to redirect to login 
def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if "userid" in request.session:
            user = request.session['userid']
            print("User >> ", user)
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return _wrapped_view

def alogin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if "adminid" in request.session:
            user = request.session['adminid']
            print("Admin >> ", user)
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/alogin/')
    return _wrapped_view





@alogin_required
def user_signup(request):
    if request.method == 'POST':
        
        form = userForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            status = form.cleaned_data['status']
            organization = form.cleaned_data['organization']
            phone_number = form.cleaned_data['phone_number']

            print(form.errors)
            if UserProfile.objects.filter(username=username):
                varerr="User Already Exists"
                return render(request,'cu.html',{'form':form,'varerr':varerr})
            
            s = UserProfile(username=username, password=password, status=status, 
                            organization=organization, phone_number=phone_number)
            s.save()
            return redirect('/users/')
        
        else:
            print(form.errors)
            return render(request,'cu.html', {'form':form})
        
    else:
        form = userForm
        return render(request,'cu.html', {'form':form,})
    
@login_required
def changepassword(request):

    if request.method == 'POST':
        form = changepasswordForm(request.POST)
        username=request.session['userid']

        if form.is_valid():
            password = form.cleaned_data['password']
            newpassword = form.cleaned_data['newpassword']
            c_newpassword = form.cleaned_data['c_newpassword']
            
            if UserProfile.objects.filter(username=username, password=password) and (c_newpassword==newpassword):
                
                UserProfile.objects.filter(username=username, password=password).update(password=newpassword)
            return redirect('/complaints/')

        else:
            varerr1="Input all fields"
            print("Invalid form", form.errors)
            return render(request,'changepassword.html', {'form':form,'varerr':varerr1})
    else:
        form = changepasswordForm()
        return render(request,'changepassword.html', {'form':form})
    

@alogin_required
def adminpassword(request):

    if request.method == 'POST':
        form = changepasswordForm(request.POST)
        username=request.session['adminid']

        if form.is_valid():
            password = form.cleaned_data['password']
            newpassword = form.cleaned_data['newpassword']
            c_newpassword = form.cleaned_data['c_newpassword']
            
            if AdminProfile.objects.filter(username=username, password=password) and (c_newpassword==newpassword):
                
                AdminProfile.objects.filter(username=username, password=password).update(password=newpassword)
            return redirect('/acomplaints/')

        else:
            varerr1="Input all fields"
            print("Invalid form", form.errors)
            return render(request,'adminpassword.html', {'form':form,'varerr':varerr1})
    else:
        form = changepasswordForm()
        return render(request,'adminpassword.html', {'form':form})
    
    
@alogin_required
def edit_user(request, id):
    user = get_object_or_404(UserProfile, pk=id)
    
    if request.method == 'POST':
        form = edituserForm(request.POST)
        
        if form.is_valid():
            status = form.cleaned_data['status']
            
        UserProfile.objects.filter(status=status).update(status=status)
        
        return redirect('/users/')
    
    else:
        form = edituserForm(initial={'status':user.status})
        return render(request, 'edituser.html', {'form':form})
    

def admin_signup(request):
    if request.method == 'POST':
        
        form = adminForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            status = form.cleaned_data['status']
            
            if AdminProfile.objects.filter(username = username):
                varerr1="Admin Already Exists"
                return render(request,'signup.html',{'form':form,'varerr':varerr1})
            s = AdminProfile(username=username, password=password, status=status)
            s.save()
            return redirect('/alogin/')
        
        else:
            varerr1="Input all fields"
            return render(request,'signup.html', {'form':form,'varerr':varerr1})
        
    else:
        form = adminForm()
        return render(request,'signup.html', {'form':form})
        

def user_login(request):
    
    if request.method == 'POST':
        form = login(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if UserProfile.objects.filter(username=username, password=password, status=status):
                request.session['userid'] = username
                print('Access Granted')
                return redirect('/complaints/')
            else:
                varerr='Wrong Credentials, Try Again'
                return render(request,'login.html',{'form':form,'varerr':varerr})
        else:
            return render(request,'login.html',{'form':form})
        
    else:
        form = login()
        return render(request,'login.html',{'form':form})

    
def admin_login(request):
    
    if request.method == 'POST':
        form = adminLogin(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if AdminProfile.objects.filter(username=username) and AdminProfile.objects.filter(password=password):
                request.session['adminid'] = username
                print('Access Granted')
                return redirect('/acomplaints/')
            else:
                varerr='Wrong Credentials, Try Again'
                return render(request,'alogin.html',{'form':form,'varerr':varerr})
        else:
            return render(request,'alogin.html',{'form':form})
        
    else:
        form = adminLogin()
        return render(request,'alogin.html',{'form':form})

@login_required
def logout(request):
    try:
        del request.session['userid']
    except:
        return redirect('/login/')


@alogin_required
def alogout(request):
    try:
       del request.session['adminid']
    except:
        pass
    return redirect('/alogin/')


@alogin_required
def users(request):
    users = UserProfile.objects.all()
    # admins = AdminProfile.objects.all()
    
    d=[]
    for c in users:
        from complaints.models import Organization
        org = Organization.objects.get(id=c.organization).organization_name
        a={'username':c.username, 'status':c.status, 'organization':org,
           'phone_number':c.phone_number,'id':c.id}
        d.append(a)
    
    # e=[]
    # for admin in admins:
    #     a={'username':admin.username, 'status':admin.status, 'id':admin.id}
    #     e.append(a)
        
    context = {
        'users' : d,    
        # 'admins' : e,
    }
    
    return render(request, 'users.html', context)