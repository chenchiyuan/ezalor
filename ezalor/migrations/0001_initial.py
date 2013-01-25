# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Phrase'
        db.create_table('ezalor_phrase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('common', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('undercover', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ezalor', ['Phrase'])

        # Adding model 'Game'
        db.create_table('ezalor_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('players', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phrase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ezalor.Phrase'])),
            ('undercover', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('ezalor', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Phrase'
        db.delete_table('ezalor_phrase')

        # Deleting model 'Game'
        db.delete_table('ezalor_game')


    models = {
        'ezalor.game': {
            'Meta': {'object_name': 'Game'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ezalor.Phrase']"}),
            'players': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'undercover': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'ezalor.phrase': {
            'Meta': {'object_name': 'Phrase'},
            'common': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'undercover': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ezalor']