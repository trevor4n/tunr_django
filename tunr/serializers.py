from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'nationality', 'name', 'songs',)

class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedModelSerializer(
        view_name='artist_detail',
        read_only=True
    )
    class Meta:
        model = Song
        fields = ('id', 'preview_url', 'album', 'title', 'artist')