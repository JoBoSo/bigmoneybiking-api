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
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = BikeTourSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'POST', 'DELETE'])
def bike_tour(request, name):
  try:
    data = BikeTour.objects.get(pk=name)
  except BikeTour.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = BikeTourSerializer(data)
    return Response(serializer.data)
  elif request.method == "DELETE":
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method == "POST":
    serializer = BikeTourSerializer(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET', 'POST'])
def bike_tour_pages(request):
  if request.method == 'GET':
    data = BikeTourPage.objects.all()
    serializer = BikeTourPageSerializer(data, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = BikeTourPageSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'POST', 'DELETE'])
def bike_tour_page(request, bike_tour):
  try:
    data = BikeTourPage.objects.get(bike_tour=bike_tour)
  except BikeTour.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = BikeTourPageSerializer(data)
    return Response(serializer.data)
  elif request.method == "DELETE":
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method == "POST":
    serializer = BikeTourPageSerializer(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET', 'POST'])
def bike_tour_cards(request):
  if request.method == 'GET':
    data = BikeTourCard.objects.all()
    serializer = BikeTourCardSerializer(data, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = BikeTourCardSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'POST', 'DELETE'])
def bike_tour_card(request, bike_tour):
  try:
    data = BikeTourCard.objects.get(bike_tour=bike_tour)
  except BikeTour.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = BikeTourCardSerializer(data)
    return Response(serializer.data)
  elif request.method == "DELETE":
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method == "POST":
    serializer = BikeTourCardSerializer(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
