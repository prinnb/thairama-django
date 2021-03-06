# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FoodMenuModel'
        db.create_table(u'thairamaapp_foodmenumodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('food_menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thairamaapp.FoodMenu'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'thairamaapp', ['FoodMenuModel'])

        # Deleting field 'FoodMenu.position'
        db.delete_column(u'thairamaapp_foodmenu', 'position')


    def backwards(self, orm):
        # Deleting model 'FoodMenuModel'
        db.delete_table(u'thairamaapp_foodmenumodel')

        # Adding field 'FoodMenu.position'
        db.add_column(u'thairamaapp_foodmenu', 'position',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    models = {
        u'thairamaapp.albumgallery': {
            'Meta': {'object_name': 'AlbumGallery'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'untitled'", 'max_length': '50'})
        },
        u'thairamaapp.foodcategory': {
            'Meta': {'object_name': 'FoodCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'thairamaapp.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'thairamaapp.foodmenu': {
            'Meta': {'object_name': 'FoodMenu'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'food_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.FoodCategory']"}),
            'food_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.FoodItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.MenuCategory']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'})
        },
        u'thairamaapp.foodmenumodel': {
            'Meta': {'ordering': "['position']", 'object_name': 'FoodMenuModel'},
            'food_menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.FoodMenu']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'thairamaapp.imagegallery': {
            'Meta': {'object_name': 'ImageGallery'},
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['thairamaapp.AlbumGallery']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'untitled'", 'max_length': '50'})
        },
        u'thairamaapp.menucategory': {
            'Meta': {'object_name': 'MenuCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'thairamaapp.suggestion': {
            'Meta': {'object_name': 'Suggestion'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['thairamaapp']