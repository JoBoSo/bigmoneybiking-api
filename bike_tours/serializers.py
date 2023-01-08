from rest_framework import serializers
from bike_tours.models import BikeTour

class BikeTourSerializer(serializers.ModelSerializer):
  class Meta:
    model = BikeTour
    fields = '__all__'
  