# Generated by Django 3.1.3 on 2020-12-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sensor', '0005_auto_20201202_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensortype',
            name='Description',
            field=models.TextField(max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='Type',
            field=models.TextField(max_length=40, verbose_name='Sensor Type'),
        ),
    ]
