# Generated by Django 5.0.6 on 2024-08-09 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drones_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dronecategory',
            options={'ordering': ['name']},
        ),
    ]
