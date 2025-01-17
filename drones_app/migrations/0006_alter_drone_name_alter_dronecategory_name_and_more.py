# Generated by Django 5.0.6 on 2024-08-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones_app', '0005_alter_pilot_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='dronecategory',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
