# Generated by Django 5.1.1 on 2024-11-19 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0006_position_passenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='availablity',
        ),
    ]