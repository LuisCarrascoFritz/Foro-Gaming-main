"""
URL configuration for forogaming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplication import views as app_views  # Alias para evitar conflictos de nombres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.index, name='index'),
    path('juegos_actuales/', app_views.juegos_actuales, name='juegos_actuales'),
    path('noticias/', app_views.noticias_videojuegos, name='noticias'),
    path('foro/', app_views.foro, name='foro'),
    path('registro/', app_views.registrar_usuario, name='registrar'),
    path('inicio_sesion/', app_views.iniciar_sesion, name='iniciar_sesion'),
    ]
