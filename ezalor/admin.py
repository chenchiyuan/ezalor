# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.contrib import admin
from ezalor.models import Phrase, Game

class PhraseAdmin(admin.ModelAdmin):
  pass

class GameAdmin(admin.ModelAdmin):
  pass

admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Game, GameAdmin)