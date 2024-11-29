# Generated by Django 5.0 on 2024-11-25 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafionew', '0003_alter_detalleseccion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafionew.profesor'),
        ),
        migrations.AlterUniqueTogether(
            name='seccion',
            unique_together={('curso', 'profesor')},
        ),
    ]