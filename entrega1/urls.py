"""entrega1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion.views import mostrar_libros, mostrar_peliculas, mostrar_videojuegos, BuscarLibro, BuscarPelicula, BuscarJuego, AltaLibro, AltaPelicula, AltaJuego

urlpatterns = [
    path('admin/', admin.site.urls),
    path("libros/", mostrar_libros),
    path("peliculas/", mostrar_peliculas),
    path("videojuegos/", mostrar_videojuegos),
    path("libros/buscar", BuscarLibro.as_view()),
    path("peliculas/buscar", BuscarPelicula.as_view()),
    path("videojuegos/buscar", BuscarJuego.as_view()),
    path("libros/alta", AltaLibro.as_view()),
    path("peliculas/alta", AltaPelicula.as_view()),
    path("videojuegos/alta", AltaJuego.as_view()),
]
