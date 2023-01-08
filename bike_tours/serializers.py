from rest_framework import serializers
from bike_tours.models import BikeTour, BikeTourCard, BikeTourPage

class BikeTourSerializer(serializers.ModelSerializer):
  class Meta:
    model = BikeTour
    fields = '__all__'

class BikeTourCardSerializer(serializers.ModelSerializer):
  class Meta:
    model = BikeTourCard
    fields = '__all__'

class BikeTourPageSerializer(serializers.ModelSerializer):
  class Meta:
    model = BikeTourPage
    fields = '__all__'
