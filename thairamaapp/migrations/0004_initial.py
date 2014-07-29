# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Suggestion'
        db.create_table(u'thairamaapp_suggestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'thairamaapp', ['Suggestion'])

        # Adding model 'MenuCategory'
        db.create_table(u'thairamaapp_menucategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'thairamaapp', ['MenuCategory'])

        # Adding model 'FoodCategory'
        db.create_table(u'thairamaapp_foodcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'thairamaapp', ['FoodCategory'])

        # Adding model 'FoodItem'
        db.create_table(u'thairamaapp_fooditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'thairamaapp', ['FoodItem'])

        # Adding model 'FoodMenuSorter'
        db.create_table(u'thairamaapp_foodmenusorter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'thairamaapp', ['FoodMenuSorter'])

        # Adding model 'FoodMenu'
        db.create_table(u'thairamaapp_foodmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('food_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thairamaapp.FoodItem'])),
            ('food_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thairamaapp.FoodCategory'])),
            ('menu_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thairamaapp.MenuCategory'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('food_menu_sorter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['thairamaapp.FoodMenuSorter'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'thairamaapp', ['FoodMenu'])

        # Adding model 'AlbumGallery'
        db.create_table(u'thairamaapp_albumgallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='untitled', max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'thairamaapp', ['AlbumGallery'])

        # Adding model 'ImageGallery'
        db.create_table(u'thairamaapp_imagegallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='untitled', max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'thairamaapp', ['ImageGallery'])

        # Adding M2M table for field albums on 'ImageGallery'
        m2m_table_name = db.shorten_name(u'thairamaapp_imagegallery_albums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagegallery', models.ForeignKey(orm[u'thairamaapp.imagegallery'], null=False)),
            ('albumgallery', models.ForeignKey(orm[u'thairamaapp.albumgallery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagegallery_id', 'albumgallery_id'])


    def backwards(self, orm):
        # Deleting model 'Suggestion'
        db.delete_table(u'thairamaapp_suggestion')

        # Deleting model 'MenuCategory'
        db.delete_table(u'thairamaapp_menucategory')

        # Deleting model 'FoodCategory'
        db.delete_table(u'thairamaapp_foodcategory')

        # Deleting model 'FoodItem'
        db.delete_table(u'thairamaapp_fooditem')

        # Deleting model 'FoodMenuSorter'
        db.delete_table(u'thairamaapp_foodmenusorter')

        # Deleting model 'FoodMenu'
        db.delete_table(u'thairamaapp_foodmenu')

        # Deleting model 'AlbumGallery'
        db.delete_table(u'thairamaapp_albumgallery')

        # Deleting model 'ImageGallery'
        db.delete_table(u'thairamaapp_imagegallery')

        # Removing M2M table for field albums on 'ImageGallery'
        db.delete_table(db.shorten_name(u'thairamaapp_imagegallery_albums'))


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