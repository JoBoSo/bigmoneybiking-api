# Generated by Django 4.1.5 on 2023-01-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_tours', '0005_alter_biketour_days_alter_biketour_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biketour',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Description'),
        ),
    ]
