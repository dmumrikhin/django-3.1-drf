# Generated by Django 4.2.4 on 2023-08-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={},
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]