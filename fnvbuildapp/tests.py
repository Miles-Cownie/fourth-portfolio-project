from django.test import TestCase
from .models import CharacterBuild


class CharacterBuildTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CharacterBuild.objects.create(title='Divine', excerpt='Testing the build')

    def test_title_label(self):
        character_build = CharacterBuild.objects.get(id=1)
        field_label = character_build._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_excerpt_label(self):
        character_build = CharacterBuild.objects.get(id=1)
        field_label = character_build._meta.get_field('excerpt').verbose_name
        self.assertEqual(field_label, 'excerpt')

    def test_title_max_length(self):
        character_build = CharacterBuild.objects.get(id=1)
        max_length = character_build._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_str_method(self):
        character_build = CharacterBuild.objects.get(id=1)
        expected_object_name = character_build.title
        self.assertEqual(str(character_build), expected_object_name)
