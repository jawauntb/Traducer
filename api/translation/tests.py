# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Translations
from .serializers import TranslationSerializer
from googletrans import Translator


def translates(input_text):
    # # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
    txt = input_text
    translator = Translator()
    translation = translator.translate(txt, dest='en')
    trans = {'language': translation.src, 'eng': translation.text}
    return [trans['language'], trans['eng']]


# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_translation(input_text="", language="", output_text=""):
        if input_text != "":
            translation = translates(input_text)
            language = translation[0]
            output_text = translation[1]
            Translations.objects.create(input_text=input_text, language=language, output_text=output_text)

    def setUp(self):
        # add test data
        self.create_translation("si quieres un nuevo trabajo")
        self.create_translation("Tienes que mostrarles que eres capaz.")
        self.create_translation("Una manera de fer-ho és Completar un repte de competències")
        self.create_translation("This is how you do it")


class GetAllTranslationsTest(BaseViewTest):

    def test_get_all_translations(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("translations-all")
        )
        # fetch the data from db
        expected = Translations.objects.all()
        serialized = TranslationSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)