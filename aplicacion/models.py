from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=400)
    autor = models.CharField(max_length=200)
    año = models.IntegerField()
    
    def __str__(self):
      return f"{self.id}, {self.nombre}, {self.autor}, ({self.año})"

class Pelicula(models.Model):
    nombre = models.CharField(max_length=400)
    director = models.CharField(max_length=200)
    año = models.IntegerField()
    
    def __str__(self):
      return f"{self.id}, {self.nombre}, {self.director}, ({self.año})"

class Juegos(models.Model):
    nombre = models.CharField(max_length=400)
    desarrollador = models.CharField(max_length=200)
    año = models.IntegerField()
    
    def __str__(self):
      return f"{self.id}, {self.nombre}, {self.desarrollador}, ({self.año})"
