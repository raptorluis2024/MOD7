# Generated by Django 5.0 on 2024-11-28 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmueble', '0005_inmueble_fecha_creacion_inmueble_ultima_modificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2024, 11, 28, 22, 33, 32, 797769, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='ultima_modificacion',
            field=models.DateField(default=datetime.datetime(2024, 11, 28, 22, 33, 32, 797769, tzinfo=datetime.timezone.utc)),
        ),
    ]