from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)
    album_cover = models.ImageField(upload_to='album-art/', blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
