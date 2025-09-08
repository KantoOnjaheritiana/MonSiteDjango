from django.db import models

class Photo(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Video(models.Model):
    titre = models.CharField(max_length=200)
    # Soit URL YouTube/Vimeo, soit fichier uploadé
    video_url = models.URLField(blank=True, null=True)
    fichier = models.FileField(upload_to='videos/', blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Texte(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Blague(models.Model):
    contenu = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.contenu[:40] + '...') if len(self.contenu) > 40 else self.contenu

