from django.shortcuts import render
from django.http import JsonResponse
from .models import Sensor, Measurement


def index(request):
    sensors = Sensor.objects.order_by('CreationDate').values()
    context = {'sensors': sensors}

    return render(request, 'Sensor/index.html', context)


def sensor_details(request, sensor_id):
    sensors = Sensor.objects.order_by('CreationDate').values()
    # current_sensor = Sensor.objects.filter(id=sensor_id)
    current_sensor = sensor_id

    context = {'sensors': sensors, 'current_sensor': current_sensor}
    return render(request, 'Sensor/index.html', context)


def sensor_measurements(request, sensor_id):
    measurements = Measurement.objects.filter(Sensor=sensor_id).order_by('Date').values()

    return JsonResponse(list(measurements), safe=False)
