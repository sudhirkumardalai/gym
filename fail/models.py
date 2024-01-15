from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    username=None
    phno=models.IntegerField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    bio=models.CharField(max_length=200)
    img=models.ImageField(upload_name="profile")
    USERNAME_FIELD=['phno']
    REQUIRED_FIELDS=[]

