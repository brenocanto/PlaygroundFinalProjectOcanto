from django.db import models
from ckeditor.fields import RichTextField

class Cancion(models.Model):
    titulo= models.CharField(max_length=50)
    album= models.CharField(max_length=50)
    letra = RichTextField()
    fecha_lanzamiento= models.DateField()
    
    def __str__(self):
        return f'{self.titulo} ({self.album})'