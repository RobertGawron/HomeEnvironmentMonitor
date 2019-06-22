from django.db import models

# Create your models here.

from django.db import models


class TemperatureMeassurement(models.Model):
    sample_value = models.DecimalField(max_digits=6, decimal_places=2)
    sample_date = models.DateTimeField('date published')

class HumidityMeassurement(models.Model):
    sample_value = models.DecimalField(max_digits=6, decimal_places=2)
    sample_date = models.DateTimeField('date published')

