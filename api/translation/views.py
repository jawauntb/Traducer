# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from .models import Translations
from .serializers import TranslationSerializer
from googletrans import Translator
from rest_framework.response import Response
from rest_framework.views import status


# Create your views here.
def translates(input_text):
    # # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
    txt = input_text
    translator = Translator()
    translation = translator.translate(txt, dest='en')
    trans = {'language': translation.src, 'eng': translation.text}
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