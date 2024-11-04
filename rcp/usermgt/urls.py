from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('alogin/', views.admin_login, name='alogin'),
    
    path('signup/', views.user_signup, name='signup'),
    path('asignup/', views.admin_signup, name='asignup'),
    
    path('logout/', views.logout, name='logout'),
    path('alogout/', views.alogout, name='alogout'),
    
    path('users/', views.users, name="users"),
    path('edituser/<int:id>/', views.edit_user, name="edituser"),


    path('changepassword/', views.changepassword, name="changepassword"),
    path('adminpassword/', views.adminpassword, name="adminpassword"),
    
]