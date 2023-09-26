from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publicacion

class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'

class VistaDetalleBlog(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'
    context_object_name = 'publicacion'

class VistaCrearEntradaBlog(CreateView):
    model = Publicacion
    template_name = 'pub_nueva.html'
    fields = ['titulo', 'autor', 'cuerpo']

class VistaEditarEntradaBlog(UpdateView):
    model = Publicacion
    template_name = 'editar_pub.html'
    fields = ['titulo', 'cuerpo']

class VistaEliminarEntradaBlog(DeleteView):
    model = Publicacion
    template_name = 'eliminar_publicacion.html'
    success_url = reverse_lazy('inicio')