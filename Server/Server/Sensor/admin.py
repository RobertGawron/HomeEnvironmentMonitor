from django.contrib import admin
from .models import Sensor, SensorType, Measurement

admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Measurement)
