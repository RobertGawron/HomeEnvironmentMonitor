from django.urls import path

from . import views

urlpatterns = [
    path('',  views.index),
    path('<int:sensor_id>/data/', views.sensor_measurements),
    path('<int:sensor_id>', views.sensor_details),
]
