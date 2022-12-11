from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=400)
    autor = models.CharField(max_length=200)
    año = models.IntegerField()
    
    def __str__(self):
      return f"{self.id}, {self.nombre}, {self.autor}, ({self.año})"
