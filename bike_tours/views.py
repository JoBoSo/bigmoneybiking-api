from bike_tours.models import BikeTour, BikeTourCard, BikeTourPage
from bike_tours.serializers import BikeTourSerializer, BikeTourCardSerializer, BikeTourPageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def bike_tours(request):
  if request.method == 'GET':
    data = BikeTour.objects.all()
    serializer = BikeTourSerializer(data, many=True)
    return Response({'bike_tours': serializer.data})
  elif request.method == "POST":
    serializer = BikeTourSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'bike_tour': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'POST', 'DELETE'])
def bike_tour(request, id):
  try:
    data = BikeTour.objects.get(pk=id)
  except BikeTour.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = BikeTourSerializer(data)
    return Response({'bike_tour': serializer.data})
  elif request.method == "DELETE":
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method == "POST":
    serializer = BikeTourSerializer(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'bike_tour': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  