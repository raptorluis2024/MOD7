# Generated by Django 5.1.4 on 2024-12-10 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
