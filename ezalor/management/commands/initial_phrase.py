# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from django.conf import settings
from ezalor.models import Phrase
import os

class Command(BaseCommand):
  def handle(self, *args, **options):
    path = os.path.join(settings.PROJECT_HOME, 'data', 'phrase.dict')
    file = open(path, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
      info = line.decode('utf-8').strip()
      common, under = info.split('——')
      phrase = Phrase(common=common.strip(), undercover=under)
      phrase.save()
      print(common.strip())
      print(under.strip())