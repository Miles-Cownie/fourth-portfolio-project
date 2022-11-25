from django.contrib import admin
from .models import CharacterBuild, Traits, TagSkills, Perks, StartingSkills, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CharacterBuild)
class BuildAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'build_gender')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    summernote_fields = ('__all__')


@admin.register(Traits, TagSkills, Perks, StartingSkills)
class SpecialAdmin(SummernoteModelAdmin):

    summernote_fields = ('__all__')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'body', 'charactercomment',
                    'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
