from django.shortcuts import render #Importado para nuestros accesos directos
from django.http import HttpResponseRedirect #Nos ayuda a la lectura de la base de datos y sus datos
from django.urls import reverse_lazy #Genera la URL hasta que es necesaria

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin #Importa para usar el sistema de logueo
from django.views import generic


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin): #Nuestra clase para sistema de logueo

    login_url = "bases:login" #Realizar el loguin
    raise_exception = False #si hay un error tendra que volver a ingresar datos
    redirect_field_name = "redirect_to" #Redirecciona al home/inicio

    def handle_no_permission(self):#Nos da permisos para el uso de nuestro usuario y contraseña
        from django.contrib.auth.models import AnonymousUser #Importa nuestro usuario
        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:sin_privilegios' #Los permisos que tiene el usuario normal
        return HttpResponseRedirect(reverse_lazy(self.login_url)) #Genera la URL


def home(request):
    from solicitudes.models import Solicitud #Importa lo que puede realizar el usuario

    becas = Solicitud.objects.count()
    b = Solicitud.objects.filter(entrega='ENTREGADO').count() #Aqui va a mostrar si el usuario le fue entregada
    n = Solicitud.objects.filter(entrega='NO ENTREGADO').count()#Aqui le mostrara si no le fue entregada

    return render(request, 'bases/home.html', {'becas': becas, 'b': b, 'n': n}) #Nos retorna al inicio


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login" #LA url de los logueos del usuario
    template_name = "bases/sin_privilegios.html" #Al entrar al usuario no tendra permisos de administrador
