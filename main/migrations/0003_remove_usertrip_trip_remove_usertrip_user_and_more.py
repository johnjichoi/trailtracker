# Generated by Django 4.2.5 on 2023-09-09 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_usertrip_trip_id_remove_usertrip_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertrip',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='usertrip',
            name='user',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
        migrations.DeleteModel(
            name='UserTrip',
        ),
    ]