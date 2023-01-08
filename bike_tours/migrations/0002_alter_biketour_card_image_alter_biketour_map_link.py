# Generated by Django 4.1.5 on 2023-01-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biketour',
            name='card_image',
            field=models.ImageField(upload_to='files/images/bike_tours/card_images'),
        ),
        migrations.AlterField(
            model_name='biketour',
            name='map_link',
            field=models.URLField(),
        ),
    ]
