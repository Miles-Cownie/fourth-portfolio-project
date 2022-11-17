from django.shortcuts import render
from django.views import generic
from .models import CharacterBuild

# List of Character Builds


class BuildList(generic.ListView):
    model = CharacterBuild
    queryset = CharacterBuild.objects.filter(status=2).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 8
