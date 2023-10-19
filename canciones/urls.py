from django.urls import path
from canciones import views

urlpatterns = [
    path("cancion/", views.CancionListView.as_view(), name="cancion"),
    path("cancion/crear/",views.CancionCreateView.as_view(),name="crear_cancion"),
    path("cancion/<int:pk>/",views.CancionDetailView.as_view(), name="detalle_cancion"),
    path("cancion/<int:pk>/editar/",views.CancionUpdateView.as_view(), name="editar_cancion"), 
    path("cancion/<int:pk>/eliminar/", views.CancionDeleteView.as_view(), name="eliminar_cancion"),
    ]