from django.urls import path
from .import views

urlpatterns = [
    # path('', views.index, name="incomes"),
    
    #User Operations
    path('addcomplaint/', views.add_complaint, name="addcomplaint"),
    path('complaints/', views.view_complaints, name="complaints"),
    path('editcomplaint/<int:id>/', views.edit_complaint, name="editcomplaint"),
    
    
    #Admin Operations
    path('acomplaints/', views.aview_complaints, name="acomplaints"),
    path('deletecomplaint/<int:id>/', views.delete_complaint, name="deletecomplaint"),
    
    path('addsoftware/', views.add_software, name="addsoftware"),
    path('editsoftware/<int:id>/', views.edit_software, name="editsoftware"),
    path('deletesoftware/<int:id>/', views.delete_software, name="deletesoftware"),
    
    path('organizations/', views.add_organization, name="organizations"),
    path('editorganization/<int:id>/', views.edit_organization, name="editorganization"),
    path('deleteorganization/<int:id>/', views.delete_organization, name="deleteorganization"),
    
    path('stats1/', views.software_count, name="stats1"),
    path('stats2/', views.stats2, name="stats2"),        

]