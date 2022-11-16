from django.contrib import admin
from .models import CharacterBuild
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CharacterBuild)
class BuildAdmin(SummernoteModelAdmin):

    summernote_fields = ('__all__')
