from django.shortcuts import render
from aplicacion.models import Libro

def literatura(request):
    return render(request, "aplicacion/literatura.html")

def mostrar_libros(request):
  lista_libros = Libro.objects.all()
  return render(request, "aplicacion/literatura.html", {"lista_libros": lista_libros})