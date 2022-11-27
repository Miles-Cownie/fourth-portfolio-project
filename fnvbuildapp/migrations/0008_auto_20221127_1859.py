# Generated by Django 3.2.16 on 2022-11-27 18:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fnvbuildapp', '0007_auto_20221127_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traits',
            name='trait_detail',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='traits',
            name='trait_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Trait Image'),
        ),
    ]