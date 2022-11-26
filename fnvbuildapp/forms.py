from .models import Comment, CharacterBuild
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BuildForm(forms.ModelForm):
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
            )
