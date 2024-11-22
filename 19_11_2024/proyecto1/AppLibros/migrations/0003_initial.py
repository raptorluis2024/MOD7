# Generated by Django 5.0 on 2024-11-22 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppLibros', '0002_remove_autorlibro_autor_remove_autorlibro_libro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AutorLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_por', models.CharField(max_length=50)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppLibros.autor')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppLibros.libro')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='libros',
            field=models.ManyToManyField(through='AppLibros.AutorLibro', to='AppLibros.libro'),
        ),
    ]
