"""
URL configuration for canineHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from model_Users import views
#from modelUser import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.routers')),
    #path('admin/listar_usuarios/', views.ListarUsuarios, name='listar_usuarios'),
    #path('admin/crear_usuario/', views.CrearUsuario, name='crear_usuario'),
    #path('', views.home, name='home'),
    #path('register/', views.register, name='register'),
    #path('task/', views.task, name='task'),
    #path('logout/', views.logoutuser, name='logout'),
    #path('login/', views.loginuser, name='login'),
]"""

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from caninos.views import CaninoViewSet
from pedidos.views import PedidoViewSet
from model_Users.views import UserViewSet
from testimonios.views import TestimonioViewSet

router = DefaultRouter()
router.register(r'caninos', CaninoViewSet)  # Esto crea las rutas CRUD para Canino
router.register(r'pedidos', PedidoViewSet)  # Esto crea las rutas CRUD para Pedido
router.register(r'users', UserViewSet)  # Esto crea las rutas CRUD para User
router.register(r'testimonios', TestimonioViewSet)  # Esto crea las rutas CRUD para Testimonio

urlpatterns = [
    path('api/', include(router.urls)),  # Añade las rutas a la URL base /api/

]
