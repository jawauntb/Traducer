# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from .models import Translations
from .serializers import TranslationSerializer
# Create your views here.


class ListTranslationsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Translations.objects.all()
    serializer_class = TranslationSerializer
