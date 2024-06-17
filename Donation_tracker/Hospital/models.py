from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} Hospital {self.address}"
