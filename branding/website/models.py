from django.db import models

# Create your models here.

class Contact(models.Model):
    name =  models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False)