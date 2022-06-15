from django.contrib import admin
from .models import Socio, Profesor

# Register your models here.


admin.site.register(Profesor)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'email', 'telefono','inicio', 'vencimiento', 'aldia', 'estado', 'cuota')
    search_fields = ('id','nombre', 'apellido','estado')
    list_filter = ('id', 'nombre',  'estado', 'registro', 'vencimiento')





