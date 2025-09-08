from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # page d'accueil
    path('photos/', views.liste_photos, name='photos'),
    path('videos/', views.liste_videos, name='videos'),
    path('textes/', views.liste_textes, name='textes'),
    path('blagues/', views.liste_blagues, name='blagues'),
]
