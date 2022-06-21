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
    path('socios_no_activos', views.socios_no_activos, name='socios_no_activos'),
    path('actualizacion_exitosa', views.actualizacion_exitosa, name='actualizacion_exitosa'),
    path('actualizar_socio/<str:pk>/', views.actualizar_socio, name='actualizar_socio'),
    path('eliminar_socio/<str:pk>/', views.eliminar_socio, name='eliminar_socio'),
    path('eliminacion_exitosa', views.eliminacion_exitosa, name='eliminacion_exitosa')
    
]
