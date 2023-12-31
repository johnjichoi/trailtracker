# Generated by Django 4.2.5 on 2023-09-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_tripphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='distance_kilometre',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='duration_hour',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='elevation_gain_metre',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='elevation_loss_metre',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
