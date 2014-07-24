from thairamaapp.models import MenuCategory, AlbumGallery
from django.http import Http404

def menu_category(request):
	menu_cats = MenuCategory.objects.all()
	return {'menu_cats': menu_cats}

def album_gallery(request):
	albums = AlbumGallery.objects.all()
	return {'albums': albums}
