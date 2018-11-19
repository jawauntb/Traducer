# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Translations(models.Model):
    # translation input text
    input_text = models.CharField(max_length=255, null=False)
    # language of input
    language = models.CharField(max_length=255, null=False)
    # english translation of text
    output_text = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}, {}, {}".format(self.input_text, self.language, self.output_text)
