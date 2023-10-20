from django.shortcuts import render, redirect
from datetime import datetime
from inicio.models import Mensaje
from inicio.forms import MensajeBusquedaFormulario, CrearMensajeFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    datos = {
        "fecha": datetime.now()
    }
    
    return render(request,r"inicio\inicio.html", datos)

def crear_mensaje(request):
    
    if request.method == "POST":
        formulario = CrearMensajeFormulario(request.POST)
        if formulario.is_valid():       
            data = formulario.cleaned_data
            mensaje = Mensaje(nombre=data.get("nombre"), mensaje=data["mensaje"])
            mensaje.save()
            return redirect("mensajes")
        else:  
            return render(request, r"inicio\crear_mensaje.html", {"formulario": formulario})
    
    formulario = CrearMensajeFormulario() 
    return render(request,r"inicio\crear_mensaje.html", {"formulario": formulario})

def listado_mensajes(request):
    formulario = MensajeBusquedaFormulario(request.GET)
    if formulario.is_valid():       
        nombre_a_buscar = formulario.cleaned_data.get("nombre")
        mensajes_encontrados = Mensaje.objects.filter(nombre__icontains=nombre_a_buscar)
         
    else:  
         mensajes_encontrados = Mensaje.objects.all()
    
    formulario = MensajeBusquedaFormulario() 
    return render(request,r"inicio\listado_mensajes.html", {"formulario": formulario,"mensajes_encontrados":mensajes_encontrados})

def about(request):
    return render(request, r"inicio\about.html")

def reparacion(request):
    return render(request, r"inicio\reparacion.html")