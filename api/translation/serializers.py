from rest_framework import serializers
from .models import Translations


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translations
        fields = ("input_text", "language", "output_text")