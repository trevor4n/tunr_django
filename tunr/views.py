from django.shortcuts import render, redirect
# Django REST Framework - JSON Responses in Django
from django.http import JsonResponse

from .models import Artist, Song
from .forms import ArtistForm

def artist_list(req):
    artists = Artist.objects.all()  # artists QuerySet
    # request argument, render template, dictionary
    return render(req, 'tunr/artist_list.html', {'artists': artists}) 
    # ...
    # Django REST Framework - JSON Responses in Django (similar to Express)
    # artists = Artist.objects.all().values('name', 'nationality', 'photo_url') # only grab some attributes from our database, else we can't serialize it.
    # artists_list = list(artists) # convert our artists to a list instead of QuerySet
    # return JsonResponse(artists_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.
    # ...
    

def song_list(req):
    songs = Song.objects.all()
    return render(req, 'tunr/song_list.html', {'songs': songs})

def artist_detail(req, pk):
    # artist = Artist.objects.get(id=pk)
    # return render(req, 'tunr/artist_detail.html', {'artist': artist})
    try:
        artist = Artist.objects.get(id=pk)
    except:
        artist = {
            'name': 'No artist found',
            'nationality':  f'with id {pk}'
        }
        print(f"artist with id={pk} didn't work")
    return render(req, 'tunr/artist_detail.html', {'artist': artist})

def song_detail(req, pk):
    try:
        song = Song.objects.get(id=pk)
    except:
        song = {
            'title': 'No song found'
        }
        print(f"song with id={pk} didn't work")
    return render(req, 'tunr/song_detail.html', {'song': song})

def artist_create(req):
    if req.method == 'POST':
        # pass
        # form = {}
        form = ArtistForm(req.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(req, 'tunr/artist_form.html', {'form': form})

def artist_edit(req, pk):
    artist = Artist.objects.get(pk=pk)
    if req.method == 'POST': # html forms are limited to POST & GET w/o s/t s/a fetch
        form = ArtistForm(req.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(req, 'tunr/artist_form.html', {'form': form})

def artist_delete(req, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')
