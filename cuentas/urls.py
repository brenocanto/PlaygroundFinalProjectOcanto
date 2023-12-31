from django.urls import path
from cuentas.views import login, registro, editar_perfil, CambiarContraseña, perfil_base
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('registrarse/', registro, name='registro'),
    path('perfil/', perfil_base, name='perfil_base'),
    path('perfil/editar', editar_perfil, name="editar_perfil"),
    path('perfil/editar/contraseña/',CambiarContraseña.as_view(), name="editar_pass"),
]