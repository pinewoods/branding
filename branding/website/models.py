from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Contact(models.Model):
    name =  models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=16, blank=True, null=True,validators=[
        RegexValidator(
            regex=r'^\+?[\d{1,2}]?\d{8,16}$',
            message='Invalid phone number',
            code='invalid_phone'
        ),
    ])
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False)