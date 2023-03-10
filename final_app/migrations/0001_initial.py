# Generated by Django 4.1.5 on 2023-01-02 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=150)),
                ('nombre', models.CharField(max_length=150)),
                ('precio_compra', models.FloatField(max_length=150)),
                ('precio_venta', models.FloatField(max_length=150)),
                ('fecha_compra', models.DateField()),
                ('fecha_registro', models.DateField(default=datetime.datetime(2023, 1, 2, 10, 51, 32, 835006))),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
    ]
