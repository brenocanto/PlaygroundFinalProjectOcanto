from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    