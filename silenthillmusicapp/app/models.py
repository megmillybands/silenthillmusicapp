from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)
    album_cover = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    audio_file = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
