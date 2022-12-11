from django import forms
from aplicacion.models import Libro, Pelicula, Juegos

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=400)

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'autor', 'año']

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'director', 'año']

class JuegosForm(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = ['nombre', 'desarrollador', 'año']