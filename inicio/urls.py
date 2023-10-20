from django.urls import path
from inicio.views import inicio,crear_mensaje, listado_mensajes,  about,reparacion

urlpatterns = [
    path("", inicio, name="inicio"),
    # path("crear-curso/<str:titulo>/<int:numero>", crear_curso, name="crear_curso"),
    path("mensajes/", listado_mensajes, name="mensajes"),
    path("mensajes/crear/", crear_mensaje, name="crear_mensaje"),
    path("about/", about, name="sobre_mi"),   
    path("reparacion/", reparacion, name="reparacion"),

    ]

    
 
