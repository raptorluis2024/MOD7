# Generated by Django 5.1.2 on 2024-12-02 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmueble', '0006_inmueble_precio_alter_inmueble_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2024, 12, 2, 14, 45, 13, 254522, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='ultima_modificacion',
            field=models.DateField(default=datetime.datetime(2024, 12, 2, 14, 45, 13, 254522, tzinfo=datetime.timezone.utc)),
        ),
    ]
