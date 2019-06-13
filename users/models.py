from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.db.models import Case, CharField, Value, When

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, default = "")
    email = models.EmailField(max_length=254, default = "")
    course = models.CharField(max_length=255, default = "")
    
    # @property
    # def available_mods(self):
    #     if self.course in ['AJ 101 Fall 2019']:
    #         return ["1", "2", "3", "4", "5", "6", "7"]
    #     else:
    #         return ["1", "2"]


