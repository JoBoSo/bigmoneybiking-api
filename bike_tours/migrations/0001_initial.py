# Generated by Django 4.1.5 on 2023-01-08 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeTour',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('card_image', models.CharField(max_length=100)),
                ('distance', models.IntegerField()),
                ('days', models.IntegerField()),
                ('dates', models.CharField(max_length=100)),
                ('map_link', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=10000)),
            ],
        ),
    ]
