from bike_tours.models import BikeTour
from django.http import JsonResponse
from bike_tours.serializers import BikeTourSerializer

def bike_tours(request):
  data = BikeTour.objects.all()
  serializer = BikeTourSerializer(data, many=True)
  return JsonResponse({'bike_tours': serializer.data})