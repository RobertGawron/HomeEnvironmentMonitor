# Generated by Django 3.1.3 on 2020-12-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sensor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='State',
            field=models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1),
            preserve_default=False,
        ),
    ]
