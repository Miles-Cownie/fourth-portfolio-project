# Generated by Django 3.2.16 on 2022-11-16 15:18

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Awaiting Approval'), (2, 'Published')], default=0)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Build Image')),
                ('excerpt', models.TextField(blank=True)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fnv_build_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Perks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perk_name', models.CharField(max_length=150)),
                ('perk_detail', models.TextField()),
                ('perk_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Perk Image')),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('perception', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('endurance', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('charisma', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('intelligence', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('agility', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('luck', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='StartingSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barter', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(52)])),
                ('energy_weapons', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
                ('explosives', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
                ('guns', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
                ('lockipick', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(47)])),
                ('medicine', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(52)])),
                ('melee_weapons', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
                ('repair', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(52)])),
                ('science', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(52)])),
                ('sneak', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(47)])),
                ('speech', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(52)])),
                ('survival', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(47)])),
                ('unarmed', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
            ],
        ),
        migrations.CreateModel(
            name='TagSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_skill_name', models.CharField(max_length=150)),
                ('skill_detail', models.TextField()),
                ('skill_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Skill Image')),
            ],
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_name', models.CharField(max_length=150)),
                ('trait_detail', models.TextField()),
                ('trait_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Trait Image')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('charactercomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fnvbuildapp.characterbuild')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='build_gender',
            field=models.ManyToManyField(to='fnvbuildapp.Gender'),
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='build_perks',
            field=models.ManyToManyField(blank=True, to='fnvbuildapp.Perks'),
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='build_special',
            field=models.ManyToManyField(to='fnvbuildapp.Special'),
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='build_starting_skills',
            field=models.ManyToManyField(blank=True, to='fnvbuildapp.StartingSkills'),
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='build_tag_skills',
            field=models.ManyToManyField(to='fnvbuildapp.TagSkills'),
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='build_traits',
            field=models.ManyToManyField(blank=True, to='fnvbuildapp.Traits'),
        ),
        migrations.AddField(
            model_name='characterbuild',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='fnv_build_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
