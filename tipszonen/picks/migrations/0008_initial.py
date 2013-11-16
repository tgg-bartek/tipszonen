# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pick'
        db.create_table(u'picks_pick', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('matchup', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('match_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('selection', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('stake', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('bookmaker', self.gf('django.db.models.fields.CharField')(default='Pinnacle', max_length=30)),
            ('odds', self.gf('django.db.models.fields.FloatField')()),
            ('analysis', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('expert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picks.ExpertCategory'])),
            ('match_score', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('pick_outcome', self.gf('django.db.models.fields.CharField')(default='?', max_length=20)),
        ))
        db.send_create_signal(u'picks', ['Pick'])

        # Adding model 'ExpertCategory'
        db.create_table(u'picks_expertcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'picks', ['ExpertCategory'])


    def backwards(self, orm):
        # Deleting model 'Pick'
        db.delete_table(u'picks_pick')

        # Deleting model 'ExpertCategory'
        db.delete_table(u'picks_expertcategory')


    models = {
        u'picks.expertcategory': {
            'Meta': {'ordering': "['-name']", 'object_name': 'ExpertCategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'picks.pick': {
            'Meta': {'ordering': "['-created_at', 'matchup']", 'object_name': 'Pick'},
            'analysis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bookmaker': ('django.db.models.fields.CharField', [], {'default': "'Pinnacle'", 'max_length': '30'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expert': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picks.ExpertCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_date': ('django.db.models.fields.DateTimeField', [], {}),
            'match_score': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'matchup': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'odds': ('django.db.models.fields.FloatField', [], {}),
            'pick_outcome': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '20'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'selection': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'stake': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['picks']