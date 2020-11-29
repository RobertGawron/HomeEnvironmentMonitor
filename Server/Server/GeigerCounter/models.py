from django.db import models

class Measurement(models.Model):
    date = models.DateTimeField('date')
    value = models.IntegerField('value')

    def __str__(self):
        return '{} {}'.format(self.date, self.value)