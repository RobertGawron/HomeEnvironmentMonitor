from django.contrib import admin
from .models import TemperatureMeassurement, HumidityMeassurement

# Register your models here.

admin.site.register(TemperatureMeassurement)
admin.site.register(HumidityMeassurement)

