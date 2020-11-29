from django.shortcuts import render

from .models import Measurement



def index(request):
    measurements = Measurement.objects.order_by('-date')

    context = {'measurements': measurements}
    return render(request, 'GeigerCounter/index.html', context)