# Generated by Django 5.0 on 2024-11-28 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmueble', '0004_tipo_inmueble_tipo_usuario_profile_inmueble'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date(2024, 11, 28)),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='ultima_modificacion',
            field=models.DateField(default=datetime.date(2024, 11, 28)),
        ),
    ]