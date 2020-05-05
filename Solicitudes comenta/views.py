from django.shortcuts import render, redirect #Son los accesos directos y la redirección
from django.views import generic #importa listas genericas

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy #Crea la URL cuando es necesario
from django.contrib.auth.decorators import login_required, permission_required #Recurre a la seguridadpara loguearse y los permisos que recibe elusuario
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin #Marca los errores de logueo
from django.http import HttpResponse #Para visualizar la pagina que es requerida en el momento
from datetime import datetime  #para la importación y manipulación de fecha y hora
from django.contrib import messages

from django.contrib.auth import authenticate #Importa para realizar la autenticación del usuario

from bases.views import SinPrivilegios #Los privilegios que recibe el usuario

from .models import Solicitud #de modelos se importa solicitud
from .forms import SolicitudForm #de formas se importa las formas de la solicitud

from reportlab.pdfgen import canvas #de reporte importa los metodos figuras, imagen, texto.
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Image #de reporte importa para la creación del documento, tabla de estilos y imagen
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle #de reporte se importa los estilos
from reportlab.lib import colors #de reportes se importan los colores
from reportlab.lib.pagesizes import letter, A4, inch, elevenSeventeen #de reporte se importa el tamaño de letra, su tipo
from reportlab.platypus import Table
from io import BytesIO #Los datos del archivo en bytes
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY #de reporte se importa la posición del cuerpo dentro del documento
from becas import settings


class SolicitudView(generic.ListView): #visualizaicón de la solicitud
    model = Solicitud #El modelo
    template_name = "solicitudes/becas_list.html"  #Lo que se va a mostrar a la persona de las listas de solicitudes
    context_object_name = "bec"
    permission_required = "solicitud.view_solicitud" #Los permisos de la solicitud


def entregados(request): #La función nos muestra las entregadas
    en = Solicitud.objects.filter(entrega='ENTREGADO') #Nos mostrara si nuestra fue entregada
    return render(request, 'solicitudes/entregasi_list.html', {'en': en})
    #Retornara a las listas y la entrega aparecera en la lista

def no_entregados(request): #La función nos muestra las no entregadas
    en = Solicitud.objects.filter(entrega='NO ENTREGADO')
    return render(request, 'solicitudes/entregano_list.html', {'en': en})
    #Retornara a las listas y en esta caso no aparecera en listas

class SolicitudNew(SinPrivilegios, SuccessMessageMixin, generic.CreateView): #Dentro de esta clase es para realizar nuevas solicitudes
    model = Solicitud #Nuestro modelo solicitud
    template_name = "solicitudes/becas_form.html" #lo que visualizara el usuario en la web solicitud y las formas de becas
    form_class = SolicitudForm #Nuestra clase formas, solicitud de formas
    success_url = reverse_lazy("solicitudes:beca_list")
    permission_required = "solicitud.add_solicitud" #Los permisos para agregar esa solicitud
    context_object_name = 'obj'
    success_message = "Registro Agregado Satisfactoriamente" #La impresión de pantalla

    def form_valid(self, form): #La función valida la forma/solicitud
        form.instance.uc = self.request.user #Dependiendo la instancia te pedira ingresar un dato faltante.
        return super().form_valid(form) #retorna a la validación de la forma


class SolicitudEdit(generic.UpdateView): #Nuestra clase llamada solicitudeditar
    model = Solicitud
    template_name = "solicitudes/becas_form.html" #Visualizar solicitudes y becas
    context_object_name = 'obj'
    form_class = SolicitudForm #Manda llamar a las formas requeridas en la solicitud
    success_url = reverse_lazy("solicitudes:beca_list")
    success_message = "Solicitud Editada" #Muestra que fueron editados los datos
    permission_required = "solicitud.change_solicitud" #Ve si existen los permisos para esas modificaciónes


def delete(request, solicitud_id): #función eliminar
    # Recuperamos la instancia de la persona y la borramos
    instancia = Solicitud.objects.get(id=solicitud_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('/solicitudes/solicitud')


def reporte(request, pk):#Función para generar reportes

    response = HttpResponse(content_type='application/pdf') #Para que la pagina permita visualizar un pdf
    report = generarPDF(pk) #Reporte que se generara en pdf
    buff = BytesIO() #El tipo de dato de información donde se almacena
    doc = SimpleDocTemplate(buff,
                            pagesize=A4,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=30,
                            bottomMargin=18,
                            )  #Es el tamaño de su estructura en que se generara el pdf
    doc.build(report) #Construye el reporte
    response.write(buff.getvalue())
    buff.close() #Para cerra el pdf
    return response #nos regresa a la opción response.


def texto(texto, tamanio): #Función de texto para reporte
    styles = getSampleStyleSheet() #Estilo de letra y formato
    style = 'Heading{}'.format(tamanio) #tamaño del archivo y texto
    return Paragraph(texto, styles[style]) #retorna a el texto y estilos de texto


def generarPDF(pk): #Función generar pdf
    title1 = ParagraphStyle('parrafos',
                            alignment=TA_CENTER,
                            fontSize=20,
                            fontName="Times-Bold",
                            spaceAfter=30,
                            spaceBefore=0
                            ) #Mostrara el titulo dentro del pdf, su tamaño, tipo de letra, donde se situa

    body = ParagraphStyle('parrafos',
                          alignment=TA_JUSTIFY,
                          fontSize=12,
                          fontName="Courier",
                          leftIndent=36,
                          spaceAfter=20,
                          spaceBefore=20
                          ) #El cuerpo dentro del pdf, tamaño, tipo de letra y donde se situa
    # header_bold = ParagraphStyle('parrafos',
    # alignment=TA_CENTER,
    # fontSize=15,
    # fontName="Times-Bold",
    # spaceAfter=5,
    # spaceBefore=15
    # )

    info = [] #La iformación del usuario
    I = Image(settings.PATH_MEDIA+'ljr.jpg')
    I.drawHeight = 1.0*inch
    I.drawWidth = 1.0*inch
    I.hAlign = 'LEFT'

    info.append(I)

    e = Solicitud.objects.get(pk=pk)

    title_ = Paragraph("SOLICITUD DE BECA 2020 ", title1) #Todo esto va dentro del cuerpo del pdf o visualización del admin
    info.append(title_)
    info.append(Paragraph("NOMBRE: {}".format(e.nombre), body))
    info.append(Paragraph("APELLIDO PATERNO: {}".format(e.ap), body))
    info.append(Paragraph("APELLIDO MATERNO: {}".format(e.am), body))
    info.append(Paragraph("DOMICILIO: {}".format(e.domicilio), body))
    info.append(Paragraph("COLONIA: {}".format(e.colonia), body))
    info.append(Paragraph("TELEFONO: {}".format(e.telefono), body))
    info.append(Paragraph("FECHA DE NACIMIENTO: {}".format(e.fn), body))
    info.append(Paragraph("GRADO ACADEMICO: {}".format(e.ga), body))
    info.append(Paragraph("MATRICULA: {}".format(e.matricula), body))
    info.append(Paragraph("FORMACIÓN ARTISTICA: {}".format(
        e.formacion_artistica), body))
    info.append(Paragraph("MODALIDAD: {}".format(e.modalidad), body))
    info.append(Paragraph("GENERO: {}".format(e.genero), body))
    info.append(Paragraph("CORREO: {}".format(e.correo), body))
    return info #Retorna a info
