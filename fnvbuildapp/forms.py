from .models import Comment, CharacterBuild
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CharacterBuildForm(forms.ModelForm):
    class Meta:
        model = CharacterBuild
        fields = (
            'title',
            'featured_image',
            'excerpt',
            'description',
            'gender',
            'strength',
            'perception',
            'endurance',
            'charisma',
            'intelligence',
            'agility',
            'luck',
            'traits',
            'tag_skills',
            'perks',
            'barter',
            'energy_weapons',
            'explosives',
            'guns',
            'lockpick',
            'medicine',
            'melee_weapons',
            'repair',
            'science',
            'sneak',
            'speech',
            'survival',
            'unarmed',
            )
        labels = {
            'title': ('Character Name'),
            'featured_image': ('Build Image'),
            'traits': ('Character Traits'),
            'tag_skills': ('Tagged Skills'),
            'perks': ('Recommended Perks'),
        }
        widgets = {
            'gender': forms.RadioSelect(),
            'traits': forms.CheckboxSelectMultiple(),
            'perks': forms.CheckboxSelectMultiple(),
            'tag_skills': forms.CheckboxSelectMultiple(),
        }
