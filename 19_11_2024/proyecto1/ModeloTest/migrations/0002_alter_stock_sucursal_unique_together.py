# Generated by Django 5.0 on 2024-11-22 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModeloTest', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock_sucursal',
            unique_together={('medicamento', 'sucursal')},
        ),
    ]
