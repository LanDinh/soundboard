from django.core.exceptions import ValidationError
from django.db import models


def get_sound_file_path(instance, filename):
    return f'sounds/{instance.origin.name}/{instance.language}/{filename}'
    
    
class Locale:
    EN_US = 'en-US'
    DE_DE = 'de-DE'
    
    choices = [
        (EN_US, EN_US),
        (DE_DE, DE_DE),
    ]


class Rating:
    GOOD = 'good'
    BAD = 'bad'

    choices = [
        (GOOD, 'Good'),
        (BAD, 'Bad'),
    ]


class FileType:
    MP3 = 'audio/mp3'
    WAV = 'audio/wav'

    choices = [
        (MP3, MP3),
        (WAV, WAV),
    ]

    def from_filename(name):
        if name.endswith('.mp3'):
            return FileType.MP3
        elif name.endswith('.wav'):
            return FileType.WAV
        else:
            return None


class Origin(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def validate_file(file):
    if FileType.from_filename(file.name) is None:
        raise ValidationError('Unsupported file type')


class Sound(models.Model):
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, related_name='sounds')
    name = models.CharField(max_length=1000)
    file = models.FileField(upload_to=get_sound_file_path, validators=[validate_file])
    type = models.CharField(max_length=30, choices=FileType.choices)
    transcription = models.TextField(blank=True)
    language = models.CharField(max_length=10, choices=Locale.choices)
    rating = models.CharField(max_length=5, choices=Rating.choices, blank=True, default='')

    def save(self, *args, **kwargs):
        self.type = FileType.from_filename(self.file.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.name, self.file.name)
