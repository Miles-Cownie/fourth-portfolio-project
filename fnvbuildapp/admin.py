from django.contrib import admin
from .models import CharacterBuild, Special
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CharacterBuild, Special)
class BuildAdmin(SummernoteModelAdmin):

    summernote_fields = ('__all__')
