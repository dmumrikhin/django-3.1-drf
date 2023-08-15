# Generated by Django 4.2.4 on 2023-08-15 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Температура')),
                ('time', models.DateTimeField(auto_now=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
            options={
                'verbose_name': 'Измерение',
                'verbose_name_plural': 'Измерения',
            },
        ),
    ]