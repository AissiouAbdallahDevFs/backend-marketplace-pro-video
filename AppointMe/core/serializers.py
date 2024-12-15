from rest_framework import serializers
from .models import Professional, Reservation

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ['id', 'user', 'specialty', 'rate']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'client', 'professional', 'start_time', 'end_time', 'status']
