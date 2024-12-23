# Generated by Django 5.1.1 on 2024-11-19 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0005_remove_bitcointransaction_cryptomus_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('card_id', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=15)),
                ('recharge', models.CharField(max_length=50)),
                ('famount', models.CharField(max_length=50)),
                ('balance', models.CharField(max_length=45)),
                ('availablity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.position')),
            ],
        ),
    ]
