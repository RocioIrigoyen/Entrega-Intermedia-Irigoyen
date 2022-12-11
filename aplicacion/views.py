from django.shortcuts import render
from aplicacion.models import Libro, Pelicula, Juegos
from aplicacion.forms import Buscar, LibroForm, PeliculaForm, JuegosForm
from django.views import View

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

class BuscarLibro(View):
    form_class = Buscar
    template_name = 'aplicacion/buscar_libro.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_libros = Libro.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_libros':lista_libros})
        return render(request, self.template_name, {"form": form})

class BuscarPelicula(View):
    form_class = Buscar
    template_name = 'aplicacion/buscar_pelicula.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_peliculas = Pelicula.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_peliculas':lista_peliculas})
        return render(request, self.template_name, {"form": form})

class BuscarJuego(View):
    form_class = Buscar
    template_name = 'aplicacion/buscar_juego.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_videojuegos = Juegos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_videojuegos':lista_videojuegos})
        return render(request, self.template_name, {"form": form})

class AltaLibro(View):

    form_class = LibroForm
    template_name = 'aplicacion/alta_libros.html'
    initial = {"nombre":"", "autor":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el libro {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaPelicula(View):

    form_class = PeliculaForm
    template_name = 'aplicacion/alta_peliculas.html'
    initial = {"nombre":"", "director":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la película {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaJuego(View):

    form_class = JuegosForm
    template_name = 'aplicacion/alta_videojuegos.html'
    initial = {"nombre":"", "desarrollador":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el videojuego {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})