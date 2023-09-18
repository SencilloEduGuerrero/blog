from django.views.generic import ListView, DetailView
from .models import Publicacion

class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'

class VistaDetalleBlog(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'
    context_object_name = 'publicacion'