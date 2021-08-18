from django.shortcuts import render

from .models import Artist, Song
# Create your views here.
def artist_list(req):
    artists = Artist.objects.all()  # artists QuerySet
    return render(req, 'tunr/artist_list.html', {'artists': artists}) # request argument, render template, dictionary

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
    