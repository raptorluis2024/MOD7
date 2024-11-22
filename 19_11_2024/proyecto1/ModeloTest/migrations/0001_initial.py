# Generated by Django 5.0 on 2024-11-22 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(auto_created=True)),
                ('cantidad', models.IntegerField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ModeloTest.medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ModeloTest.comuna')),
                ('medicamento', models.ManyToManyField(through='ModeloTest.Stock_Sucursal', to='ModeloTest.medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='stock_sucursal',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ModeloTest.sucursal'),
        ),
    ]
