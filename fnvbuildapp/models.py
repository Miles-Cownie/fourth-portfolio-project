from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Status variable

STATUS = ((0, "Draft"), (1, "Awaiting Approval"), (2, "Published"))


class Gender(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.gender

# SPECIAL stats Model


class Special(models.Model):
    strength = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    perception = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    endurance = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    charisma = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    intelligence = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    agility = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    luck = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )

    def __str__(self):
        return [
            self.strength,
            self.perception,
            self.endurance,
            self.charisma,
            self.agility,
            self.intelligence,
            self.luck
            ]

# Character Build Model


class CharacterBuild(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="fnv_build_author"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('Build Image', default='placeholder')
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    build_gender = models.ManyToManyField(Gender)
    build_special = models.ManyToManyField(Special)
    build_traits = models.ManyToManyField(Traits)
    build_tag_skills = models.ManyToManyField(TagSkills)
    build_perks = models.ManyToManyField(Perks)
    build_starting_skills = models.ManyToManyField(StartingSkills)
    likes = models.ManyToManyField(
        User, related_name='fnv_build_like', blank=True
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
