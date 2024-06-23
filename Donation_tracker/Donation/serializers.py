from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('first_name', 'second_name', 'email', 'phone_number', 'town', 'date_of_birth', 'blood_type', 'gender', 'last_donation', 'created_at', 'updated_at')
