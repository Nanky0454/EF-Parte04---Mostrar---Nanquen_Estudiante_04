# Generated by Django 4.1.5 on 2023-01-02 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=150)),
                ('nombre', models.CharField(max_length=150)),
                ('horas', models.IntegerField()),
                ('creditos', models.IntegerField()),
                ('fecha_registro', models.DateField(default=datetime.datetime(2023, 1, 2, 11, 8, 46, 823645))),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 11, 8, 46, 823645)),
        ),
    ]