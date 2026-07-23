import os
from django.shortcuts import render, get_object_or_404
from .models import *
import cloudinary
import cloudinary.utils

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True
)


def home(request):
    return render(request, "home.html")

def silenthillone(request):
    album = Album.objects.get(name='Silent Hill 1')
    songs = Song.objects.filter(album=album)

    context = {'songs': songs}
    return render(request, "silenthill1.html", context)

def silenthilltwo(request):
    album = Album.objects.get(name='Silent Hill 2')
    songs = Song.objects.filter(album=album)

    context = {'songs': songs}
    return render(request, "silenthill2.html", context)

def silenthillthree(request):
    album = Album.objects.get(name='Silent Hill 3')
    songs = Song.objects.filter(album=album)

    context = {'songs': songs}
    return render(request, "silenthill3.html", context)

def player(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    
    albumone = Song.objects.filter(album=1)
    albumtwo = Song.objects.filter(album=2)
    albumthree = Song.objects.filter(album=3)

    artwork_url, _ = cloudinary.utils.cloudinary_url(
        str(song.album.album_cover),
        resource_type="image"
    )

    audio_url, _ = cloudinary.utils.cloudinary_url(
        str(song.audio_file),
        resource_type="video"
    )

    context = {
        'song': song,
        'title': song.title,
        'artist': "Akira Yamaoka",
        'album': song.album,
        'artwork_url': artwork_url,
        'audio_url': audio_url,
        'albumone': albumone,
        'albumtwo': albumtwo,
        'albumthree': albumthree,
    }

    return render(request, "player.html", context)
