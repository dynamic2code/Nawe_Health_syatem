from rest_framework import serializers
from .models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ('first_name', 'second_name', 'email', 'phone_number', 'town', 'date_of_birth', 'blood_type', 'gender', 'last_donation', 'created_at', 'updated_at')
