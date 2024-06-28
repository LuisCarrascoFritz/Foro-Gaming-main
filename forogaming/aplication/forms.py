from django import forms
from .models import CartItem
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']



class RegistroForm(UserCreationForm):
    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'rut', 'nombre', 'correo', 'password1', 'password2')

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password')