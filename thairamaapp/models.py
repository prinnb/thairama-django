from django.db import models
import datetime
from django.utils import timezone
from decimal import Decimal
import hashlib
# Create your models here.


class Suggestion(models.Model):
	"""
	Model to store suggestion from customer
	"""
	name = models.CharField(max_length=50)
	email = models.EmailField()
	post_date = models.DateTimeField('date posted', auto_now = True)
	content = models.TextField()   
	def __unicode__(self):
		return u"%s" % self.id

class MenuCategory(models.Model):
	"""
	Model to store categories of menu (e.g, dinner, lunch, etc.)
	"""
	name = models.CharField(max_length=50, unique = True)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class FoodCategory(models.Model):
	"""
	Model to store categories of food (e.g, noodle, sandwich, etc.)
	"""
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	def __unicode__(self):
		return self.name

class FoodItem(models.Model):
	"""
	Model to store food item and its detail
	"""
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to = 'images/FoodItem/', blank=True)
	def __unicode__(self):
		return self.name

class FoodMenuSorter(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
		return self.name
		
class FoodMenu(models.Model):
	"""
	Model to represent menu of a restaurant where each tuple refer to a food item in a food category in a menu category
	"""
	food_item = models.ForeignKey(FoodItem)
	food_cat = models.ForeignKey(FoodCategory)	
	menu_cat = models.ForeignKey(MenuCategory)
	price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	food_menu_sorter = models.ForeignKey(FoodMenuSorter)
	position = models.PositiveSmallIntegerField("Position")

	class Meta:
		ordering = ['position']
	def __unicode__(self):
		return self.food_item.name + " | " + self.menu_cat.name

class AlbumGallery(models.Model):
	"""
	Model to represent gallery album
	"""
	name = models.CharField(max_length=50, default = "untitled")
	description = models.TextField(null=True, blank=True)
	position = models.PositiveSmallIntegerField("Position")
	class Meta:
		ordering = ['position']
	def __unicode__(self):
		return self.name
        
class ImageGallery(models.Model):
	"""
	Model to represent gallery image
	"""
	name = models.CharField(max_length=50,  default = "untitled")
	image = models.ImageField(upload_to = 'images/ImageGallery')
	thumb = models.ImageField(upload_to = 'images/ImageGallery/thumb', null=True)
	albums = models.ForeignKey(AlbumGallery)
	position = models.PositiveSmallIntegerField("Position")
	class Meta:
		ordering = ['position']
	def __unicode__(self):
		return self.name


