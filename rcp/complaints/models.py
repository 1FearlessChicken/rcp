from urllib import request
from django.db import models
from django.utils.timezone import now
from usermgt.views import *



class Complaints(models.Model):
    organization = models.CharField(max_length=256, null=False, default='Ruffwal')
    complaint = models.CharField()
    date = models.DateField(default=now, )
    resolution = models.CharField()
    owner = models.CharField()
    software = models.CharField(max_length=256, null=False, default='Ruffs')
    
    
    def __str__(self):
        return self.complaint
    
    
class Software(models.Model):
    software_name = models.CharField()
    
    def __str__(self):
        return self.software_name
    

class Organization(models.Model):
    organization_name = models.CharField()
    email = models.CharField()
    phone_number = models.CharField()
    
    def __str__(self):
        return self.organization_name