from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['Flight_No', 'Airline', 'From', 'To', 'Duration', 'Price']
