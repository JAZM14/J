from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta: #Clase de metadatos para poder tener mejor control de datos
        model = Solicitud
        fields = ['nombre', 'ap', 'am', 'domicilio', 'colonia', 'telefono', 'fn', 'ga', 'matricula',
                  'formacion_artistica', 'modalidad', 'genero', 'correo', 'entrega'] #Es una tupla de datos
        widget = {'fn': forms.DateInput}

    def __init__(self, *args, **kwargs): #definimimos la función para poder saltar un argumento o que sea opcional
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): #Utilizamos el bucle y pedimos leer fields
            self.fields[field].widget.attrs.update({  #lee los datos de la tupla y el widget los asignan a los campos de los formularios
                'class': 'form-control'
            })
