from django.contrib import admin
from bike_tours.models import BikeTour, BikeTourCard, BikeTourPage

class BikeTourCardAdmin(admin.ModelAdmin):
  readonly_fields = ['img_preview']

admin.site.register(BikeTour)
admin.site.register(BikeTourCard, BikeTourCardAdmin)
admin.site.register(BikeTourPage)