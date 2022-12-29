from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from blog_terror.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, "blog_terror/index.html")

class PostList(ListView):
    model = Post

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("blog-terror-listar")
    fields = '__all__'

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("blog-terror-listar")
    fields = '__all__'

class PostDetalle(DetailView):
    model = Post

class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("blog-terror-listar")


