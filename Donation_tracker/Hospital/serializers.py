from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('name', 'address', 'town', 'phone_number', 'email', 'created_at', 'updated_at')
        