# Generated by Django 4.1.5 on 2023-01-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_tours', '0002_alter_biketour_card_image_alter_biketour_map_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeTourCard',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='files/images/bike_tours/card_images')),
            ],
        ),
        migrations.RenameField(
            model_name='biketour',
            old_name='distance',
            new_name='distance_km',
        ),
    ]
