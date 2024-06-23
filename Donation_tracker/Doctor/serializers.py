from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('hospital', 'first_name', 'second_name', 'email', 'phone_number')
