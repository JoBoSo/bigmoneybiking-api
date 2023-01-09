# Generated by Django 4.1.5 on 2023-01-09 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bike_tours', '0011_biketour_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biketourcard',
            name='bike_tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bike_tours.biketour'),
        ),
        migrations.AlterField(
            model_name='biketourpage',
            name='bike_tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bike_tours.biketour'),
        ),
    ]
