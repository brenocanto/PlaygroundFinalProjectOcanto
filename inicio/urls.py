from django.urls import path
from inicio.views import inicio,crear_mensaje, listado_mensajes, editar_mensaje, eliminar_mensaje, detalle_mensaje, about,reparacion
urlpatterns = [
    path("", inicio, name="inicio"),
    # path("crear-curso/<str:titulo>/<int:numero>", crear_curso, name="crear_curso"),
    path("mensajes/", listado_mensajes, name="mensajes"),
    path("mensajes/crear/", crear_mensaje, name="crear_mensaje"),
    path("mensajes/<int:mensaje_id>/editar/", editar_mensaje, name="editar_mensaje"),
    path("mensajes/<int:mensaje_id>/eliminar/", eliminar_mensaje, name="eliminar_mensaje"),
    path("mensajes/<int:mensaje_id>/",detalle_mensaje, name="detalle_mensaje"),
    path("about/", about, name="sobre_mi"),   
    path("reparacion/", reparacion, name="reparacion"),

    ]