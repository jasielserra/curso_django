from django.shortcuts import render

# Create your views here.
from pypro.aperitivos.models import Video

videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 251224475),
    Video('instalacao-windows', 'Instalação Windows', 251497668),
    ]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    #slug = str(slug)
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
