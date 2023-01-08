from django.db import models
import datetime # don't remove.
from django.utils.html import mark_safe

class BikeTour(models.Model):
  name = models.CharField('Name', max_length=100, primary_key=True, default='create unique name')
  description = models.CharField('Description', max_length=100)
  distance_km = models.IntegerField('Distance (km)')
  start_date = models.DateField('Start Date')
  end_date = models.DateField('End Date')

  @property
  def days(self):
    return (self.start_date - self.end_date).days

  def __str__(self) -> str:
    return self.name


class BikeTourCard(models.Model):
  bike_tour = models.OneToOneField(BikeTour, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100, default='no title')
  subtitle = models.CharField(max_length=100, default='no subtitle')
  image = models.ImageField(upload_to='images/bike_tours/card_images')

  def __str__(self) -> str:
    return self.bike_tour.name

  def img_preview(self):
    return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')


class BikeTourPage(models.Model):
  bike_tour = models.OneToOneField(BikeTour, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100, default='no title')
  map_url = models.URLField()
  report = models.CharField(max_length=10000, default='no report')

  def __str__(self) -> str:
    return self.bike_tour.name
