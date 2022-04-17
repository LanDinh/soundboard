from django.contrib import admin

from .models import Origin, Sound

# Register your models here.
admin.site.register(Origin)

class SoundAdmin(admin.ModelAdmin):
    readonly_fields = ('type',)


admin.site.register(Sound, SoundAdmin)
