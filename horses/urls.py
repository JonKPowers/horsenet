from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'), 
    path('horses.html', views.horses, name='horses'),
    path('races.html', views.races, name='races'),
    path('tracks.html', views.tracks, name='tracks'),
    path('deepnet.html', views.deepnet, name='deepnet'),
]
