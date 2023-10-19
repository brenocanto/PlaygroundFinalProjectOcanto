from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class NuestroFormularioDeRegistro(UserCreationForm):
    username= forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}
        help_texts = {campo: '' for campo in fields}
        
class NuestroEditarPerfilFormulario(UserChangeForm):
    password = None
    first_name= forms.CharField(label= "Modificar Nombre", max_length=30)
    last_name= forms.CharField(label= "Modificar Apellido",max_length=50)
    email = forms.EmailField(label= "Modificar email")
    link = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model= User
        fields= ['first_name','last_name', 'email', 'link','avatar']
    