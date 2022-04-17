from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView

from .forms import SoundEditForm
from .models import Sound, Origin

# Create your views here.    
class SoundListView(ListView):
    
    model = Origin
    template_name = 'sound_list.html'
    
    def get_queryset(self):
        return Origin.objects.prefetch_related('sounds').all().order_by('name')

    def post(self, request):
        sound = Sound.objects.get(pk=request.POST.get('id'))
        form = SoundEditForm(request.POST, instance=sound)
        if not form.is_valid():
            raise ValidationError(form.errors.as_json())
        form.save()
        return HttpResponseRedirect('/data#next-{}'.format(sound.pk))
        
def get_sound(request, id):
    sound = Sound.objects.get(id=id)
    filename = sound.file.name.split('/')[-1]
    response = HttpResponse(sound.file, content_type=sound.type)
    return response
