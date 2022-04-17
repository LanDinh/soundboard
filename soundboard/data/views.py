from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Sound, Origin

# Create your views here.    
class SoundListView(ListView):
    
    model = Origin
    template_name = 'sound_list.html'
    
    def get_queryset(self):
        return Origin.objects.prefetch_related('sounds').all().order_by('name')
        
def get_sound(request, id):
    sound = Sound.objects.get(id=id)
    filename = sound.file.name.split('/')[-1]
    response = HttpResponse(sound.file, content_type=sound.type)
    return response
