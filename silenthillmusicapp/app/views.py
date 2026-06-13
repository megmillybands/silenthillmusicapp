from django.shortcuts import render
from .models import *


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
    song = Song.objects.get(id=song_id)
    albumone = Song.objects.filter(album=1)
    albumtwo = Song.objects.filter(album=2)
    albumthree = Song.objects.filter(album=3)

    context = {
        'song': song,
        'title': song.title,
        'artist': "Akira Yamaoka",
        'album': song.album,
        'artwork_url': song.album.album_cover.url,
        'audio_url': song.audio_file.url,
        'albumone': albumone,
        'albumtwo': albumtwo,
        'albumthree': albumthree,
    }

    return render(request, "player.html", context)