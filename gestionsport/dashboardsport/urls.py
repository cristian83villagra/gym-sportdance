from django.urls import path
from . import views 




urlpatterns = [
    path('', views.index, name='index'),
    path('agregar', views.agregar, name='agregar'),
    path('envio_exitoso', views.envio_exitoso, name='envio_exitoso'),
    path('clientes', views.clientes, name='clientes'),
    path('no_activos', views.no_activos, name='no_activos'),
    path('consulta', views.consulta, name='consulta'),
    path('estadisticas', views.estadisticas, name='estadisticas'),
    #path('paginacion', views.paginacion, name='paginacion')
    
]
