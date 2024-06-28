from django.shortcuts import render
from forogaming import settings
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, InicioSesionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from aplication.models import Product
# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def juegos_actuales(request):
    return render(request, 'web/juegos_actuales.html')

def foro(request):
    return render(request,'web/foro.html')

def noticias_videojuegos(request):
    api_key = settings.NEWS_API_KEY
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'video games',
        'language': 'es', 
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    articles = response.json()['articles']
    context = {
        'articles': articles
    }
    return render(request, 'web/noticias.html', context)


@login_required
def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)
    context = {'cart': cart}
    return render(request, 'cart/carrito.html', context)

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def update_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    new_quantity = request.POST.get('quantity')
    cart_item.quantity = new_quantity
    cart_item.save()
    return redirect('view_cart')


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.refresh_from_db()  # Actualizar datos del usuario con los datos del formulario
            usuario.rut = form.cleaned_data.get('rut')
            usuario.nombre = form.cleaned_data.get('nombre')
            usuario.correo = form.cleaned_data.get('correo')
            usuario.save()
            raw_password = form.cleaned_data.get('password1')
            usuario = authenticate(username=usuario.username, password=raw_password)
            login(request, usuario)
            return redirect('inicio')  # Ajusta 'inicio' al nombre de la URL a la que quieres redirigir tras el registro
    else:
        form = RegistroForm()
    return render(request, 'web/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')  # Ajusta 'inicio' al nombre de la URL a la que quieres redirigir tras el inicio de sesión
    else:
        form = InicioSesionForm()
    return render(request, 'web/inicio_sesion.html', {'form': form})