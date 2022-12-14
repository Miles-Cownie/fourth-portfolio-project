from django.contrib import admin
from .models import CharacterBuild, Traits, TagSkills, Perks, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CharacterBuild)
class BuildAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'gender')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    summernote_fields = ('__all__')
    actions = ['approve_build']

    def approve_build(self, request, queryset):
        queryset.update(status=2)


@admin.register(Traits, TagSkills, Perks)
class SpecialAdmin(SummernoteModelAdmin):

    summernote_fields = ('__all__')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'body', 'character_build',
                    'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
