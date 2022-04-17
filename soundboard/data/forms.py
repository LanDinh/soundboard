from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm
from .models import Sound

class SoundEditForm(ModelForm):
    class Meta:
        model = Sound
        fields = ['name', 'transcription']
