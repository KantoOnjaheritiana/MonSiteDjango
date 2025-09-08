from django.shortcuts import render
from .models import Photo, Video, Texte, Blague
from django.core.paginator import Paginator

def photos_view(request):
    photos = Photo.objects.all().order_by('-date_pub')  # les plus récentes en premier
    return render(request, 'photos.html', {'photos': photos})


def home(request):
    carousel_photos = Photo.objects.all()[:5]  # Les 5 dernières photos par exemple
    return render(request, 'home.html', {'carousel_photos': carousel_photos})

def videos_view(request):
    videos = Video.objects.all().order_by('-date_pub')
    return render(request, 'videos.html', {'videos': videos})


def textes(request):
    textes_list = Texte.objects.all().order_by('-date_pub')
    paginator = Paginator(textes_list, 4)  # 4 textes par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'contenu/textes.html', {'page_obj': page_obj})




def home(request):
    # un petit dashboard de tes derniers contenus
    ctx = {
        'photos': Photo.objects.order_by('-date_pub')[:6],
        'videos': Video.objects.order_by('-date_pub')[:6],
        'textes': Texte.objects.order_by('-date_pub')[:5],
        'blagues': Blague.objects.order_by('-date_pub')[:5],
    }
    return render(request, 'contenu/home.html', ctx)

def liste_photos(request):
    return render(request, 'contenu/photos.html', {'photos': Photo.objects.order_by('-date_pub')})

def liste_videos(request):
    return render(request, 'contenu/videos.html', {'videos': Video.objects.order_by('-date_pub')})

def liste_textes(request):
    return render(request, 'contenu/textes.html', {'textes': Texte.objects.order_by('-date_pub')})

def liste_blagues(request):
    return render(request, 'contenu/blagues.html', {'blagues': Blague.objects.order_by('-date_pub')})

