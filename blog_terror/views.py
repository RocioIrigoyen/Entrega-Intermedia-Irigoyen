from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from blog_terror.models import Post, Mensaje
from django.urls import reverse_lazy
from blog_terror.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "blog_terror/index.html")

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("blog-terror-listar")
    fields = '__all__'

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("blog-terror-listar")
    fields = '__all__'

class PostDetalle(DetailView):
    model = Post

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog-terror-listar")

class UserSignup(CreateView):
    form_class = UsuarioForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("blog-terror-listar")

class UserLogin(LoginView):
    next_page = reverse_lazy("blog-terror-listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy("blog-terror-listar")

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("blog-terror-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("blog-terror-mensajes-listar")

