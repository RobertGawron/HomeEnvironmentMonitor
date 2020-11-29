from django.shortcuts import render

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