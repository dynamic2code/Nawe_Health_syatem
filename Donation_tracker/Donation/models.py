from django.db import models
from Donor.models import Donor
from Hospital.models import Hospital
from Doctor.models import Doctor

# Create your models here.
DONATION_TYPE_CHOICES = (
    ('blood', 'Blood'),
    ('money', 'Money'),
    ('medication', 'Medication'),
)
PAYMENT_METHOD_CHOICES = (
    ('cash', 'Cash'),
    ('credit_card', 'Credit Card'),
    ('bank_transfer', 'Bank Transfer'),
    ('paypal', 'PayPal'),
)

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete= models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE_CHOICES)
    amount = models.FloatField(null=True, blank=True)
    blood_volume = models.IntegerField(null=True, blank=True)  # pint
    hemoglobin_level = models.FloatField(null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Donation of{self.donation_type} made by{self.donor.first_name} at Hospital {self.hospital.name} by {self.doctor.first_name}"
