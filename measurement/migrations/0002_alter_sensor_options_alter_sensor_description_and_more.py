# Generated by Django 4.2.4 on 2023-08-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={},
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
