# Generated by Django 5.0.6 on 2024-08-10 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drones_app', '0003_alter_drone_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'ordering': ['-distance_value']},
        ),
    ]
