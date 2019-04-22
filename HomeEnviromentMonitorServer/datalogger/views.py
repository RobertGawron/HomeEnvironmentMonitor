from django.shortcuts import render
from django.http import HttpResponse
from .fusioncharts import FusionCharts
from django.http import JsonResponse
from .models import TemperatureMeassurement, HumidityMeassurement

def index(request):
    dataSource = {}
    dataSource['chart'] = { 
        "caption": " ",
            "subCaption": " ",
            "xAxisName": " ",
            "yAxisName": " ",
            "numberPrefix": " ",
            "theme": "zune"
        }

    dataSource['categories'] = [
    {
      "category": [ ]
    },
    {
      "category": [ ]
    }
    ]

    dataSource['dataset'] = [
    {
      "seriesname": "Temperature",
      "data": [  ]
    },
    {
      "seriesname": "Humidity",
      "data": [  ]
    },
    ]

    # TODO this is ugly, remove magic numbers
    
    for key in TemperatureMeassurement.objects.all():
        sample_date = {}
        sample_date['label'] = str((key.sample_date))
        dataSource['categories'][0]['category'].append(sample_date)
        
        sample_value = {}
        sample_value['value'] = str(int(key.sample_value))
        dataSource['dataset'][0]['data'].append(sample_value)
        
        
    for key in HumidityMeassurement.objects.all():
        sample_date = {}
        sample_date['label'] = str((key.sample_date))
        dataSource['categories'][1]['category'].append(sample_date)
        
        sample_value = {}
        sample_value['value'] = str(int(key.sample_value))
        dataSource['dataset'][1]['data'].append(sample_value)
        

    
    chartObj = FusionCharts( 'msline', 'ex1', '1200', '600', 'chart-1', 'json',dataSource )
    
    print(chartObj.render())
    return render(request, 'index.html', {'output': chartObj.render()}) 