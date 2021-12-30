import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    phone = models.CharField(max_length = 200)