# Generated by Django 5.1.2 on 2024-11-26 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafionew', '0006_alter_detalleseccion_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleseccion',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnodetalleseccion', to='desafionew.estudiante'),
        ),
    ]