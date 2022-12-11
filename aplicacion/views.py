from django.shortcuts import render
from aplicacion.models import Libro, Pelicula, Juegos

def literatura(request):
    return render(request, "aplicacion/literatura.html")

def mostrar_libros(request):
  lista_libros = Libro.objects.all()
  return render(request, "aplicacion/literatura.html", {"lista_libros": lista_libros})

def mostrar_peliculas(request):
  lista_peliculas = Pelicula.objects.all()
  return render(request, "aplicacion/peliculas.html", {"lista_peliculas": lista_peliculas})

def mostrar_videojuegos(request):
  lista_videojuegos = Juegos.objects.all()
  return render(request, "aplicacion/videojuegos.html", {"lista_videojuegos": lista_videojuegos})