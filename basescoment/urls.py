from django.urls import path #Una lista de nombre en este caso importa las urls
from django.contrib.auth import views as auth_views #La seguridad relacionada para las vistas
from bases import views as vistas # importa las vistas
from bases.views import HomeSinPrivilegios #no le da permisos de admin a los usuarios en el home

urlpatterns = [
    path('', vistas.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'),
         name='login'),#Vistas del logueo de usuarios
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'),
         name='logout'),#Deslogueo del usuario

    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),#Los permisos de admin estan limitados

]
