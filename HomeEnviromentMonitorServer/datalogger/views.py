from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TemperatureMeassurement

# Create your views here.

def index(request):
    temperature_list = TemperatureMeassurement.objects.order_by('-sample_date')
    #output = ', '.join([str(q.sample_value) for q in temperature_list])
    template = loader.get_template('datalogger/index.html')
    context = {
        'temperature_list' : temperature_list,
    }
    return HttpResponse(template.render(context, request))
