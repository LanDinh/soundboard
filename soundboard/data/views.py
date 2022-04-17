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
