from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from Donor.models import Donor
from Hospital.models import Hospital
from Doctor.models import Doctor

# Define the choices
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

STATUS_CHOICES = {
    'received': 'Received',
    'processing': 'Processing',
    'distributed': 'Distributed',
    'cancelled': 'Cancelled',
    'returned': 'Returned',
}

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE_CHOICES)
    amount = models.FloatField(null=True, blank=True)
    blood_volume = models.IntegerField(null=True, blank=True)  # pint
    hemoglobin_level = models.FloatField(null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES.items(), default='received')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Donation of {self.donation_type} made by {self.donor.first_name} at Hospital {self.hospital.name} by {self.doctor.first_name}"

# Signal handler function
@receiver(pre_save, sender=Donation)
def send_status_change_notification(sender, instance, **kwargs):
    print("status change", instance.status, instance.pk)
