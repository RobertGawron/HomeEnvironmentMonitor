from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Measurement

import datetime

def index(request):
    measurements = Measurement.objects.order_by('date')

    ## TODO this is dummy way, it's just to see if things works
    i=0
    for m in measurements:
        m.date = i
        i+=1

    context = {'measurements': measurements}
    return render(request, 'GeigerCounter/index.html', context)


def getMeasurements(request):
    measurements = Measurement.objects.order_by('date').values()
    return JsonResponse(list(measurements), safe=False)