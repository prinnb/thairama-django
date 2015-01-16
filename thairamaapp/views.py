from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from thairamaapp.models import MenuCategory,FoodMenu, FoodCategory, AlbumGallery, ImageGallery
from forms import SuggestionForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    return render(request, 'thairamaapp/index.html', {})

def credits(request):
	context = {}
	return render(request, 'thairamaapp/credits.html', context)

def contact_us(request):
	context = {}
	return render(request, 'thairamaapp/contact_us.html', context)

def press(request):
	context = {}
	return render(request, 'thairamaapp/press.html', context)

def suggestion(request):
	if request.method == 'POST': 
		form = SuggestionForm(request.POST)
		if form.is_valid():
			form.save()
			email = EmailMessage('Hello', 'World', to=['prinnb@hotmail.com'])
			email.send()
			return HttpResponseRedirect('/')

	elif request.user.is_authenticated():
		#automatically fill out name and email for logged in user
		form = SuggestionForm(initial = {'name': request.user.username, 'email': request.user.email})
	else:
		form = SuggestionForm()
	context = {}
	context.update(csrf(request))
	context['form'] = form
	return render(request, 'thairamaapp/suggestion.html', context)


def gallery(request):
	albums = AlbumGallery.objects.all()
	context = {'albums': albums}
	return render(request, 'thairamaapp/gallery.html', context)

def album(request, album_name):
	album = get_object_or_404(AlbumGallery, name=album_name)
	images = album.imagegallery_set.all()
	context = {'images': images, 'album': album}
	return render(request, 'thairamaapp/album.html', context)

def menu(request):
	menu_cats = MenuCategory.objects.all()
	context = {'menu_cats': menu_cats}
	return render(request, 'thairamaapp/menu.html', context)

def menu_cat(request, menu_cat_name):
	menu_cat = get_object_or_404(MenuCategory, name=menu_cat_name)
	food_menu_list = FoodMenu.objects.filter(menu_cat = menu_cat)
	menu_dict = {}
	food_cat_list = []
	for food_menu in food_menu_list:
		if food_menu.food_cat not in food_cat_list:
			food_cat_list.append(food_menu.food_cat)
		if food_menu.food_cat not in menu_dict:
			menu_dict[food_menu.food_cat] = [food_menu]
		else:
			menu_dict[food_menu.food_cat].append(food_menu)

	context = {'menu_cat': menu_cat, 'menu_dict' : menu_dict, 'food_cat_list' : food_cat_list}
	return render(request, 'thairamaapp/menu_cat.html', context)

