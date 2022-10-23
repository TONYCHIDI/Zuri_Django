from django.db import models

# Create your models here.


class Artiste (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateTimeField('date released')
    likes = models.IntegerField(default=0)
    artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.CharField(max_length=250)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
