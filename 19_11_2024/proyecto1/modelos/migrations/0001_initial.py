# Generated by Django 5.0 on 2024-11-20 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualización', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('dpto', models.CharField(blank=True, max_length=10, null=True)),
                ('comuna', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modelos.cliente')),
            ],
        ),
    ]
