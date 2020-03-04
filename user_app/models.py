from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name
'''
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)

    #additional info

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pic',blank=True)
    def __str__(self):
        return self.user.username
