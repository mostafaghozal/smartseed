# Generated by Django 2.1.2 on 2018-10-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_Type', '0002_auto_20181027_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='crop',
            name='location',
            field=models.FloatField(default=0.0),
        ),
    ]
