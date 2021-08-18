from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # artist list is going to be rendered in the root URL
    path('', views.artist_list, name='artist_list'), 
    # explicit songs url
    path('songs/', views.song_list, name='song_list'),
    # artist detail route
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    # song detail route
    path('songs/<int:pk>', views.song_detail, name='song_detail'),
    # artist form
    path('artists/new', views.artist_create, name='artist_create'),
]