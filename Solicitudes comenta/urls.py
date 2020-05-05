from django.urls import path, include #Framework+ includepara facilitar la conexión y  ejecución inmediatas de URLS
from solicitudes import views as vistas
from .views import SolicitudView, SolicitudNew, SolicitudEdit #Framework para importar de views.py

urlpatterns = [  #Los path son listas de directorios y buscaradonde se situan
    path('solicitud/', SolicitudView.as_view(), name="beca_list"),
    path('solicitud/nuevo', SolicitudNew.as_view(), name="beca_new"),
    path('solicitud/edit/<int:pk>', SolicitudEdit.as_view(), name="beca_edit"),
    path('delete/<int:solicitud_id>', vistas.delete, name='delete'),

    path('entregados', vistas.entregados, name='entregados'),
    path('noentregados/', vistas.no_entregados, name='noentregados'),

    path('reporte/<int:pk>', vistas.reporte, name='reporte')
]
