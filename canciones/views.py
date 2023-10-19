from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from canciones.models import Cancion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CancionCreateView(CreateView):
    model = Cancion
    template_name = "nueva/crear_cancion.html"
    fields = ["titulo","album","letra","fecha_lanzamiento"]
    success_url = reverse_lazy("cancion")
    
class CancionDeleteView(LoginRequiredMixin, DeleteView):
    model = Cancion
    template_name = "nueva/eliminar_cancion.html"
    success_url = reverse_lazy("cancion")

class CancionDetailView(DetailView):
    model = Cancion
    template_name = "nueva/detalle_cancion.html"

class CancionListView(ListView):
    model = Cancion
    context_object_name = "listado_cancion"
    template_name = "nueva/listar_cancion.html"
    
    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            canciones = self.model.objects.filter(titulo__icontains = titulo)
        else:
            canciones = self.model.objects.all()
        return canciones    
    
class CancionUpdateView(LoginRequiredMixin, UpdateView):
    model = Cancion
    template_name = "nueva/editar_cancion.html"
    fields = ["titulo","album","letra","fecha_lanzamiento"]
    success_url = reverse_lazy("cancion")
