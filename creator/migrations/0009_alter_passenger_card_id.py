# Generated by Django 5.1.1 on 2024-11-19 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0008_alter_passenger_balance_alter_passenger_card_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='card_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]