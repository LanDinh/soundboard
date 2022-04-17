from django.urls import path

from . import views

urlpatterns = [
    path('', views.SoundListView.as_view(), name='sound-list'),
    path('<int:id>/download/', views.get_sound, name='sound-file'),
]
