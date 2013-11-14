# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pick.pick_profit'
        db.delete_column(u'picks_pick', 'pick_profit')

        # Adding field 'Pick.pick_outcome'
        db.add_column(u'picks_pick', 'pick_outcome',
                      self.gf('django.db.models.fields.CharField')(default='?', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Pick.pick_profit'
        db.add_column(u'picks_pick', 'pick_profit',
                      self.gf('django.db.models.fields.CharField')(default='?', max_length=20),
                      keep_default=False)

        # Deleting field 'Pick.pick_outcome'
        db.delete_column(u'picks_pick', 'pick_outcome')


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