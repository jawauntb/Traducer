# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from .models import Translations
from .serializers import TranslationSerializer
from rest_framework.response import Response
from rest_framework.views import status
from google.cloud import translate
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'translation/My Project-09af8ab5b26a.json'

# client.translate('koszula')
# {
#     'translatedText': 'shirt',
#     'detectedSourceLanguage': 'pl',
#     'input': 'koszula',
# }


# Create your views here.
def translates(input_text):
    txt = input_text
    translate_client = translate.Client()
    translation = translate_client.translate(txt, target_language='en')
    trans = {'language': translation['detectedSourceLanguage'], 'eng': translation['translatedText']}
    return [trans['language'], trans['eng']]


class ListCreateTranslationsView(generics.ListCreateAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = Translations.objects.all()
    serializer_class = TranslationSerializer

    def post(self, request, *args, **kwargs):
        translation = translates(request.data["input_text"])
        a_trans = Translations.objects.create(
            input_text=request.data["input_text"],
            language=translation[0],
            output_text=translation[1]
        )
        return Response(
            data=TranslationSerializer(a_trans).data,
            status=status.HTTP_201_CREATED
        )

