from django.shortcuts import render

# Create your views here.

def video(request, slug):
   video = {
      'instalacao-windows':{'titulo': '', 'vimeo_id': 251497668},
      'motivacao':{'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 251224475},
   }
   video=video[slug]
   return render(request, 'aperitivos/video.html', context={'video': video})
