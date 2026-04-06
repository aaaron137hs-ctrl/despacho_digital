"""
URL configuration for despacho_digital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from expedientes.views import lista_casos # Importamos tu función de Python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_casos, name='lista'), # Esta línea dice: "Si entras a la raíz, usa lista_casos"
]

from expedientes.views import lista_casos, borrar_caso, editar_caso # Agregamos las nuevas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_casos, name='lista'),
    path('borrar/<int:id>/', borrar_caso, name='borrar'), # Nueva ruta borrar
    path('editar/<int:id>/', editar_caso, name='editar'), # Nueva ruta editar
]
