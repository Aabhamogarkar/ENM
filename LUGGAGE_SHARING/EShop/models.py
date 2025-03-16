from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#model means database.
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20, blank=True, null=True)
    # phone= models.IntegerField(None)
    # def __init__(self, name, age, email, cell_phone=None): # Now it's okay
    #     self.name = name
    #     self.age = age
    #     self.email = email
    #     self.cell_phone = cell_phone
    #unique means email should be unique.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

