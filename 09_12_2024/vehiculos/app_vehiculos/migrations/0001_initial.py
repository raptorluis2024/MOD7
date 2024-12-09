# Generated by Django 5.1.4 on 2024-12-09 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistroContabilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
                ('valor', models.FloatField()),
                ('vehiculo_id', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='RegistroVehiculo', to='app_vehiculos.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('rut', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateTimeField(auto_now_add=True)),
                ('vehiculo_id', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='ChoferVehiculo', to='app_vehiculos.vehiculo')),
            ],
        ),
    ]
