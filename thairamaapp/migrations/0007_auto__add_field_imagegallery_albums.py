# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ImageGallery.albums'
        db.add_column(u'thairamaapp_imagegallery', 'albums',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['thairamaapp.AlbumGallery']),
                      keep_default=False)

        # Removing M2M table for field albums on 'ImageGallery'
        db.delete_table(db.shorten_name(u'thairamaapp_imagegallery_albums'))


    def backwards(self, orm):
        # Deleting field 'ImageGallery.albums'
        db.delete_column(u'thairamaapp_imagegallery', 'albums_id')

        # Adding M2M table for field albums on 'ImageGallery'
        m2m_table_name = db.shorten_name(u'thairamaapp_imagegallery_albums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagegallery', models.ForeignKey(orm[u'thairamaapp.imagegallery'], null=False)),
            ('albumgallery', models.ForeignKey(orm[u'thairamaapp.albumgallery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagegallery_id', 'albumgallery_id'])


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
            'Meta': {'ordering': "['position']", 'object_name': 'FoodMenu'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'food_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.FoodCategory']"}),
            'food_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.FoodItem']"}),
            'food_menu_sorter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.FoodMenuSorter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.MenuCategory']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'})
        },
        u'thairamaapp.foodmenusorter': {
            'Meta': {'object_name': 'FoodMenuSorter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'thairamaapp.imagegallery': {
            'Meta': {'ordering': "['position']", 'object_name': 'ImageGallery'},
            'albums': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['thairamaapp.AlbumGallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'untitled'", 'max_length': '50'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'})
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