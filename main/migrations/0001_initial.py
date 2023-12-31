# Generated by Django 4.2.5 on 2023-09-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=50)),
                ('trip_date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('distance_metre', models.IntegerField()),
                ('duration_second', models.IntegerField()),
                ('elevation_gain_metre', models.IntegerField()),
                ('elevation_loss_metre', models.IntegerField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('trip_id', models.IntegerField()),
            ],
        ),
    ]
