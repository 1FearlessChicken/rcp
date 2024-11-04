from django.urls import path
from .import views
# from django.views.decorators.csrf import csrf_exempt

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
    path('deletesoftware/', views.delete_software, name="deletesoftware"),
    
    path('organizations/', views.add_organization, name="organizations"),
    path('editorganization/<int:id>/', views.edit_organization, name="editorganization"),
    path('deleteorganization/', views.delete_organization, name="deleteorganization"),
    
    path('stats1/', views.stats1, name="stats1"),
    path('stats2/', views.stats2, name="stats2"),        

]