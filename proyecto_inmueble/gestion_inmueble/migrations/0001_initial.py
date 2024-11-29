# Generated by Django 5.0 on 2024-11-27 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=40)),
                ('region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmueble.region')),
            ],
        ),
    ]