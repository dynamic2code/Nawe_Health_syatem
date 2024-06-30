from django.db import models
from Hospital.models import Hospital
from Doctor.models import Doctor
from Donor.models import Donor

HOSPITAL_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('rescheduled', 'Rescheduled'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed'),
)
# Create your models here.
class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=HOSPITAL_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for{self.donor.first_name} at  {self.hospital.name}Hospital at{self.appointment_date}"
