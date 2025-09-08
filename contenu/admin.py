from django.contrib import admin
from .models import Photo, Video, Texte, Blague

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_pub')
    search_fields = ('titre',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_pub')
    search_fields = ('titre',)

@admin.register(Texte)
class TexteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_pub')
    search_fields = ('titre', 'contenu')

@admin.register(Blague)
class BlagueAdmin(admin.ModelAdmin):
    list_display = ('contenu', 'likes', 'date_pub')
    search_fields = ('contenu',)
