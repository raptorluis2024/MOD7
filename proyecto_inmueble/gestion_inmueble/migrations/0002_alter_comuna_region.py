# Generated by Django 5.0 on 2024-11-27 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmueble', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inmueble.region'),
        ),
    ]
