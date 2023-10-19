from django import forms

class MensajeFormularioBase(forms.Form):
    nombre= forms.CharField(max_length=50)
    mensaje= forms.CharField()
    
class EditarMensajeFormulario(MensajeFormularioBase):
    ...
    
class CrearMensajeFormulario(MensajeFormularioBase):
    ...
    
class MensajeBusquedaFormulario(forms.Form):
    nombre= forms.CharField(max_length=50, required=False)
    
    