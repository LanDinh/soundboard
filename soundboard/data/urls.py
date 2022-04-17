from django.urls import path

from . import views

urlpatterns = [
    path('', views.SoundListView.as_view(), name='sound-list'),
]
