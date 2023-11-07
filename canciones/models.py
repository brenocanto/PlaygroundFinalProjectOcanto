from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Cancion(models.Model):
    titulo= models.CharField(max_length=50)
    album= models.CharField(max_length=50)
    letra = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    fecha_lanzamiento= models.DateField()
    imagen = models.ImageField(upload_to='imagenes', null= True, blank= True)
    
    def __str__(self):
        return f'{self.titulo} ({self.album}) - Usuario: {self.autor}'