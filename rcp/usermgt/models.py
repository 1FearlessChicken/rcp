from django.db import models
from django.utils.timezone import now



class UserProfile(models.Model):
    username = models.CharField()
    password = models.CharField()
    organization = models.CharField()
    phone_number = models.CharField()
    status = models.CharField()
    
    def __str__(self):
        return self.username
    
class AdminProfile(models.Model):
    username = models.CharField()
    password = models.CharField()
    status = models.CharField()
    
    def __str__(self):
        return self.username
    