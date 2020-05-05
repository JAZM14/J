from django.contrib import admin  #Framework el sitio administrativo

from .models import Solicitud  #Importamos solicitud
from import_export import resources
from import_export.admin import ImportExportModelAdmin #Framework para poder usar el admin


class SolicitudResource(resources.ModelResource):
    class Meta: #Class de metadatos
        model = Solicitud #Nuestro mdelo


class SolicitudAdmin(ImportExportModelAdmin, admin.ModelAdmin): #La clase para solicitar datos al admin y permisos
    list_display = ('nombre', 'domicilio', 'colonia', 'telefono', 'entrega') #La lista en pantalla
    search_fields = ['domicilio'] #busca los campos de domicilio
    resource_class = SolicitudResource #Manda llamar a la clase para el modelo solicitud


admin.site.register(Solicitud, SolicitudAdmin) #Permisos del administrador que permita el us0 de solicitud
