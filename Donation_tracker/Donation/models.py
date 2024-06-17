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

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete= models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE_CHOICES)
    amount = models.FloatField()
    blood_volume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Donation made by{self.donor.first_name} at Hospital {self.hospital.name} by {self.doctor.first_name}"
