from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from thairamaapp import views


admin.autodiscover()

urlpatterns = patterns('',
	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^$', views.index, name='index'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^menu/(?P<menu_cat_name>.*)/$', views.menu_cat, name='menu_cat'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^press/$', views.press, name='press'),
    url(r'^suggestion/$', views.suggestion, name='suggestion'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery/(?P<album_name>.*)/$', views.album, name='album'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
