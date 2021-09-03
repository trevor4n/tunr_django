from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
# from django.conf.urls.static import static

# DRF comes with some pre-configured conventions for URLs, in what they call a router. These URLs map to views that follow a naming convention. 
# Django can handle multiple request types in one view and using one url

urlpatterns = [
    # artist list is going to be rendered in the root URL
    # path('', views.artist_list, name='artist_list'), 
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
]