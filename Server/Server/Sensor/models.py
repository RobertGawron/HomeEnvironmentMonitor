from django.db import models


class SensorType(models.Model):
    Type = models.TextField('Sensor Type', max_length=40)
    Description = models.TextField('Description', max_length=100)

    def __str__(self):
        return self.Type


class SensorState(models.TextChoices):
    ACTIVE = u'Y', 'Active'
    INACTIVE = u'N', 'Inactive'


class Sensor(models.Model):
    Type = models.ForeignKey(SensorType, on_delete=models.CASCADE)

    Status = models.TextChoices('Sensor Status', 'Active Inactive')
    ShortName = models.TextField('Short Name', max_length=40)
    Description = models.TextField('Description', max_length=100)
    CreationDate = models.DateTimeField('Creation Date')
    State = models.CharField(max_length=1,
                             choices=SensorState.choices,
                             default=SensorState.ACTIVE)

    def __str__(self):
        return '{} : ({})'.format(self.ShortName, self.Description)


class Measurement(models.Model):
    Sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    Date = models.DateTimeField('Date')
    Value = models.IntegerField('Value')

    def __str__(self):
        return '{} {}'.format(self.Date, self.Value)
