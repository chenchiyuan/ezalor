# -*- coding: utf-8 -*-
# __author__ = chenchiyuan
from __future__ import division, unicode_literals, print_function

from django.db import models
import random

class Phrase(models.Model):
  common = models.CharField(u'普通词', max_length=64)
  undercover = models.CharField(u'卧底词', max_length=64)
  used = models.BooleanField(verbose_name=u'是否使用', default=False)

  def __unicode__(self):
    return self.common + u'-' + self.undercover

  @classmethod
  def random(cls):
    phrases = cls.objects.all()
    count = phrases.count()
    current = random.randint(0, count-1)
    return phrases[current]

class Game(models.Model):
  players = models.IntegerField(u'参赛人数', default=4)
  blank = models.BooleanField(u'是否使用白板', default=False)
  status = models.BooleanField(u'进行中', default=False)
  phrase = models.ForeignKey(Phrase, verbose_name=u'词组')
  undercover = models.IntegerField(u'卧底的号码', default=0)

  def __unicode__(self):
    return '%d' %self.players

  def save(self, force_insert=False, force_update=False, using=None):
    self.id = 1
    self.status = False
    self.undercover = random.randint(1, self.players)
    self.phrase = Phrase.random()
    return super(Game, self).save(force_insert, force_update, using)

  @classmethod
  def game(cls):
    return cls.objects.get(id=1)

  def identity(self, id):
    id = int(id)
    if id == self.undercover:
      return self.phrase.undercover
    else:
      return self.phrase.common

  def is_undercover(self, id):
    id = int(id)
    return id == self.undercover