from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('hospital', 'doctor', 'donor', 'appointment_date', 'reason', 'status')
        