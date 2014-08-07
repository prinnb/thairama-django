from django.contrib import admin
from thairamaapp.models import Suggestion, MenuCategory, FoodCategory, FoodItem, FoodMenu, FoodMenuSorter, AlbumGallery, ImageGallery


class SuggestionAdmin(admin.ModelAdmin):
    readonly_fields=('post_date',)

class FoodMenuInlineAdmin(admin.TabularInline):
    # define the sortable
    sortable_field_name = "position"
    model = FoodMenu

class FoodMenuSorterAdmin(admin.ModelAdmin):
	inlines = [
		FoodMenuInlineAdmin,
	] 

class ImageGalleryInlineAdmin(admin.TabularInline):
    # define the sortable
    sortable_field_name = "position"
    model = ImageGallery
    extra = 0

class AlbumGalleryAdmin(admin.ModelAdmin):
	inlines = [
		ImageGalleryInlineAdmin,
	]

admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(FoodItem)
admin.site.register(FoodCategory)
admin.site.register(MenuCategory)
admin.site.register(FoodMenuSorter, FoodMenuSorterAdmin)
admin.site.register(AlbumGallery, AlbumGalleryAdmin)
admin.site.register(ImageGallery)
