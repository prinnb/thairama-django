from django.contrib import admin
from thairamaapp.models import Suggestion, MenuCategory, FoodCategory, FoodItem, FoodMenu, AlbumGallery, ImageGallery

class FoodMenuInline(admin.StackedInline):
    model = FoodMenu
    extra = 0

class FoodItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
    ]
    inlines = [FoodMenuInline]

class SuggestionAdmin(admin.ModelAdmin):
    readonly_fields=('post_date',)

admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(FoodItem)
admin.site.register(FoodCategory)
admin.site.register(MenuCategory)
admin.site.register(FoodMenu)
admin.site.register(AlbumGallery)
admin.site.register(ImageGallery)

