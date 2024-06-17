from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
BLOOD_GROUP_CHOICES = (
    ('A+', 'A Positive'),
    ('A-', 'A Negative'),
    ('B+', 'B Positive'),
    ('B-', 'B Negative'),
    ('AB+', 'AB Positive'),
    ('AB-', 'AB Negative'),
    ('O+', 'O Positive'),
    ('O-', 'O Negative'),
)
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('X', 'Other'),
    ('N', 'Prefer not to say'),
)
class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    town = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    blood_type = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    last_donation = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} Hospital {self.second_name}"
