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
from aplicacion.views import mostrar_libros, mostrar_peliculas, mostrar_videojuegos, BuscarLibro, BuscarPelicula, BuscarJuego, AltaLibro, AltaPelicula, AltaJuego, ActualizarLibro, ActualizarPelicula, ActualizarJuego, BorrarLibro, BorrarPelicula, BorrarJuego
from blog_terror.views import (index, PostList, PostCrear, PostActualizar, PostBorrar, 
                               PostDetalle, UserSignup, UserLogin, UserLogout, MensajeListar,
                               MensajeBorrar, MensajeCrear, MensajeDetalle)
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView

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
    path("libros/actualizar/<int:pk>", ActualizarLibro.as_view()),
    path("peliculas/actualizar/<int:pk>", ActualizarPelicula.as_view()),
    path("videojuegos/actualizar/<int:pk>", ActualizarJuego.as_view()),
     path("libros/borrar/<int:pk>", BorrarLibro.as_view()),
    path("peliculas/borrar/<int:pk>", BorrarPelicula.as_view()),
    path("videojuegos/borrar/<int:pk>", BorrarJuego.as_view()),
    path("blog-terror/", index, name= "blog-terror-index"),
    path("blog-terror/listar/", PostList.as_view(), name= "blog-terror-listar"),
    path("blog-terror/crear/", staff_member_required(PostCrear.as_view()), name= "blog-terror-crear"),
    path("blog-terror/<int:pk>/actualizar/", staff_member_required(PostActualizar.as_view()), name= "blog-terror-actualizar"),
    path("blog-terror/<int:pk>/detalle/", PostDetalle.as_view(), name= "blog-terror-detalle"),
    path("blog-terror/<int:pk>/borrar/", staff_member_required(PostBorrar.as_view()), name= "blog-terror-borrar"),
    path("blog-terror/signup/", UserSignup.as_view(), name = "blog-terror-signup"),
    path("blog-terror/login/", UserLogin.as_view(), name = "blog-terror-login"),
    path("blog-terror/logout/", UserLogout.as_view(), name = "blog-terror-logout"),
    path("blog-terror/mensajes/crear/", MensajeCrear.as_view(), name = "blog-terror-mensajes-crear"),
    path("blog-terror/mensajes/<int:pk>/detalle/", MensajeDetalle.as_view(), name = "blog-terror-mensajes-detalle"),
    path("blog-terror/mensajes/listar/", MensajeListar.as_view(), name = "blog-terror-mensajes-listar"),
    path('blog-terror/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="blog-terror-mensajes-borrar"),
    path('blog-terror/about', TemplateView.as_view(template_name='blog_terror/about.html'), name="blog-terror-about"),
]
