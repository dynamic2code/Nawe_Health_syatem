from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Hospital.models import Hospital

# Create your models here.
class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr:{self.first_name} {self.second_name}"
