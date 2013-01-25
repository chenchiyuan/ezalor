# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from ezalor.models import Game

@csrf_exempt
def identity(request, pk):
  game = Game.game()
  if request.method == 'GET':
    identity = game.identity(pk)
  else:
    identity = u'无辜' if not game.is_undercover(pk) else '卧底'

  return render_to_response('game.html', {
    'identity': identity,
  })