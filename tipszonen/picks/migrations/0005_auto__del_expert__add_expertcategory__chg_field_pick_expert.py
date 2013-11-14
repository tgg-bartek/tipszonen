# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Expert'
        db.delete_table(u'picks_expert')

        # Adding model 'ExpertCategory'
        db.create_table(u'picks_expertcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'picks', ['ExpertCategory'])


        # Changing field 'Pick.expert'
        db.alter_column(u'picks_pick', 'expert_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picks.ExpertCategory']))

    def backwards(self, orm):
        # Adding model 'Expert'
        db.create_table(u'picks_expert', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'picks', ['Expert'])

        # Deleting model 'ExpertCategory'
        db.delete_table(u'picks_expertcategory')


        # Changing field 'Pick.expert'
        db.alter_column(u'picks_pick', 'expert_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picks.Expert']))

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
            'match_score': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'matchup': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'odds': ('django.db.models.fields.FloatField', [], {}),
            'pick': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pick_profit': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '20'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'stake': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['picks']