from django.db import models

# Create your models here.

class Artiste (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Lyric(models.Model):
    content = models.TextField('Lyrics')
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content
