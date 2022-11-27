from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Status variable

STATUS = ((0, "Draft"), (1, "Awaiting Approval"), (2, "Published"))

# Traits Model


class Traits(models.Model):
    trait_name = models.CharField(max_length=150)
    trait_detail = models.TextField()
    trait_image = CloudinaryField('Trait Image')

    def __str__(self):
        return self.trait_name

# Tagged Skills Model


class TagSkills(models.Model):
    tag_skill_name = models.CharField(max_length=150)
    skill_detail = models.TextField()
    skill_image = CloudinaryField('Skill Image')

    def __str__(self):
        return self.tag_skill_name

# Perks Model


class Perks(models.Model):
    perk_name = models.CharField(max_length=150)
    perk_detail = models.TextField()
    perk_image = CloudinaryField('Perk Image')

    def __str__(self):
        return self.perk_name

# Starting Skills Model


class StartingSkills(models.Model):

    def __str__(self):
        return f"{[self.barter,self.energy_weapons, self.explosives, self.guns, self.lockipick, self.medicine, self.melee_weapons, self.repair, self.science, self.sneak, self.speech, self.survival, self.unarmed]}"

# Character Build Model


class CharacterBuild(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

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
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.FEMALE
        )
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
    traits = models.ManyToManyField(Traits, blank=True)
    tag_skills = models.ManyToManyField(TagSkills)
    perks = models.ManyToManyField(Perks, blank=True)
    barter = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(52)
            ]
        )
    energy_weapons = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(47)
            ]
        )
    explosives = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(47)
            ]
        )
    guns = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(47)
            ]
        )
    lockpick = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(47)
            ]
        )
    medicine = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(52)
            ]
        )
    melee_weapons = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(47)
            ]
        )
    repair = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(52)
            ]
        )
    science = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(52)
            ]
        )
    sneak = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(47)
            ]
        )
    speech = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(52)
            ]
        )
    survival = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(47)
            ]
        )
    unarmed = models.IntegerField(
        default=15,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(47)
            ]
        )
    likes = models.ManyToManyField(
        User, related_name='fnv_build_like', blank=True
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('character_build', kwargs={'pk': self.pk})

# Character Build Comment Model


class Comment(models.Model):
    charactercomment = models.ForeignKey(
        CharacterBuild, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=90)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}."
