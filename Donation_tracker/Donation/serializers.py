from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('donor', 'hospital', 'doctor', 'donation_type', 'amount', 'blood_volume','status', 'created_at', 'updated_at')
