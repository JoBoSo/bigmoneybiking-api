from django.db import models

class BikeTour(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  title = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=100)
  card_image = models.CharField(max_length=100)
  distance = models.IntegerField()
  days = models.IntegerField()
  dates = models.CharField(max_length=100)
  map_link = models.CharField(max_length=100)
  report = models.CharField(max_length=10000)