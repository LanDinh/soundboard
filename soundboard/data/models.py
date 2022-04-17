from django.db import models


def get_sound_file_path(instance, filename):
    return f'data/{instance.origin.name}/{instance.language}/{filename}'
    
    
class Locale:
    EN_US = 'en-US'
    DE_DE = 'de-DE'
    
    choices = [
        (EN_US, EN_US),
        (DE_DE, DE_DE),
    ]



class Origin(models.Model):
    name = models.CharField(max_length=200)


class Sound(models.Model):
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, related_name='sounds')
    name = models.CharField(max_length=1000)
    file = models.FileField(upload_to=get_sound_file_path)
    type = models.CharField(max_length=100)
    transcription = models.TextField(blank=True)
    language = models.CharField(max_length=10, choices=Locale.choices)
