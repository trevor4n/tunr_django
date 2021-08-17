from django.urls import path
from . import views

urlpatterns = [
    # artist list is going to be rendered in the root URL
    path('', views.artist_list, name='artist_list'), 
    # explicit songs url
    path('songs/', views.song_list, name='song_list'),
]