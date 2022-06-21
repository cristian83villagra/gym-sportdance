from calendar import month
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Socio
from django.db.models import Q, F
from .forms import Form_Client
from datetime import datetime, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction



#-------------VISTA INDEX---------------#

"""
ESTA ES LA FUNCION DE LA PAGINA PRINCIPAL DE LA APLICACION
"""
def index(request):
    fecha_hoy = date.today()
    return render(request, 'dashboard/index.html', {'fecha_hoy': fecha_hoy})



#-------------VISTA VISTA AGREGAR SOCIOS---------------#

"""
Esta funcion es para agregar nuevos socios mediante un formulario y ser cargados en la base de datos

"""

def agregar(request):
    """
    Formulario para agregar usuarios nuevos
    """
    fecha_hoy = date.today()
    if request.method == 'POST':
        form = Form_Client(request.POST)
        if form.is_valid():
            form.save()
            return redirect("envio_exitoso")
    else:
        form= Form_Client
    return render(request, 'dashboard/agregar.html',{'form': form, 'fecha_hoy': fecha_hoy})



#-------------VISTA USUARIO SE AGREGO EXITOSAMENTE---------------#

def envio_exitoso(request):
    """
    Funcion que lleva a una pagina de envio formulario exitoso
    """
    return render(request, 'dashboard/envio_exitoso.html',{})


#-------------VISTA ACTUALIZAR USUARIO---------------#

def actualizar_socio(request, pk):
    """
    Funcion para actualizar socio
    """
    fecha_hoy = date.today()
    socio = Socio.objects.get(id=pk)
    form = Form_Client(instance=socio)
    if request.method == 'POST':
        form = Form_Client(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect("actualizacion_exitosa")
    
    return render(request, 'dashboard/actualizar_socio.html',{'form': form, 'fecha_hoy': fecha_hoy})

#-------------VISTA ACTUALIZACION EXITOSA---------------#

def actualizacion_exitosa(request):
    """
    Funcion que actualiza a socio
    """
    return render(request, 'dashboard/actualizacion_exitosa.html',{})



#-------------VISTA ELIMINAR USUARIO---------------#

def eliminar_socio(request, pk):
    """
    Funcion para actualizar socio
    """
    fecha_hoy = date.today()
    socio = Socio.objects.get(id=pk)
    if request.method == 'POST':
        socio.delete()
        return redirect("eliminacion_exitosa")
    context = {'item': socio, 'fecha_hoy': fecha_hoy}
    return render(request, 'dashboard/eliminar_socio.html',context)


#-------------VISTA ELIMINACION EXITOSA---------------#

def eliminacion_exitosa(request):
    """
    Funcion que lleva a una pagina de eliminacion exitosa
    """
    return render(request, 'dashboard/eliminacion_exitosa.html',{})


#-------------VISTA LISTA DE CLIENTES DEL GYM---------------#

def clientes(request):
    """
    Funcion para mostrar el listado de los socios agregados
    """
    fecha_hoy = date.today()
    clientes = Socio.objects.all()
    paginator = Paginator(clientes, 8) # 3 posts in each page
    page = request.GET.get('page')
    pagina_actual = paginator.get_page(page)
    return render(request,
        'dashboard/clientes.html',
        {'clientes': pagina_actual, 'fecha_hoy': fecha_hoy})


    
#-------------VISTA CONSULTA DE SOCIOS NO ACTIVOS---------------#

def no_activos(request):
    """
    Funcion actualiza los activos a no activos al terminar su mes de membresia.
    """
    hoy = date.today()
    #vencidos = Socio.objects.filter(estado = 'No activo')
    #print(vencidos)
    vencidos = Socio.objects.filter(vencimiento__lte = hoy).update(estado = 'No activo', aldia= 'NO', cuota=0000.00)
        
    return render(request, 'dashboard/no_activos.html', {'vencidos': vencidos} )
    


#-------------VISTA CONSULTA DE SOCIOS ---------------#
    
    """
    Formulario para consultar si un socio esta activo
    """
def consulta(request):
    fecha_hoy = date.today()
    queryset = request.GET.get("buscar")
    clientes = Socio.objects.filter(estado = True)
    if queryset:
        clientes = Socio.objects.filter(
            Q(id__exact = queryset) |
            Q(nombre__icontains = queryset)
        ).distinct()
        print(clientes)
    return render(request, 'dashboard/consulta.html', {'clientes': clientes, 'fecha_hoy':fecha_hoy})



#-------------VISTA ESTADISTICAS---------------#

"""
    Formulario para construir la vista de dashboard en construccion
"""

def estadisticas(request):
    hoy = date.today()
    hoy1 = datetime.now()
    semana = date.weekday
    mes = datetime.now()
    anio = date.year
    fecha_hoy = date.today()
    
    
    if mes.month == 4:
        registro_abril = Socio.objects.filter(registro__month = 4).count
    elif mes.month == 5:
        registro_mensual = Socio.objects.filter(registro__month = 5).count
    elif mes.month == 6:
        registro_junio = Socio.objects.filter(registro__month = 6).count
    elif mes.month == 7:
        registro_julio = Socio.objects.filter(registro__month = 7).count
    elif mes.month == 8:
        registro_agosto = Socio.objects.filter(registro__month = 8).count
    elif mes.month == 9:
        registro_septiembre = Socio.objects.filter(registro__month = 9).count
    elif mes.month == 10:
        registro_octubre = Socio.objects.filter(registro__month = 10).count
    elif mes.month == 11:
        registro_noviembre = Socio.objects.filter(registro__month = 11).count
    else:
        registro_diciembre = Socio.objects.filter(registro__month = 12).count
    
    #-----------REGISTRADOS POR DIA-----------#    
    
    registro_diario = Socio.objects.filter(inicio__day=hoy1.day).count
    
    
    #-----------REGISTRADOS POR MES-----------#    
    
    registro_mensual = Socio.objects.filter(inicio__month=mes.month).count
    
    
    #-----------ACTIVOS Y NO ACTIVOS-----------#    
    
    #muestra los socios activos
    activos = Socio.objects.filter(estado = "Activo").count
    
    #muesta los socios inactivos
    no_activos = Socio.objects.filter(estado='No activo').count
    
    
    #-----------REGISTRADOS POR MES-----------#    
    
    #registrados mes de junio
    registro_junio = Socio.objects.filter(inicio__month = 6).count
    ingreso_junio = Socio.objects.filter(inicio__month = 6).aggregate(Sum('cuota'))
    junio= ingreso_junio['cuota__sum']
    
    #registrados mes de julio
    registro_julio = Socio.objects.filter(inicio__month = 7).count
    ingresos_julio = Socio.objects.filter(inicio__month = 7).aggregate(Sum('cuota'))
    julio= ingresos_julio['cuota__sum']
    
    #registrados mes de agosto
    registro_agosto = Socio.objects.filter(inicio__month = 8).count
    ingresos_agosto = Socio.objects.filter(inicio__month = 8).aggregate(Sum('cuota'))
    agosto= ingresos_agosto['cuota__sum']
    
    #registrados mes de septiembre
    registro_septiembre = Socio.objects.filter(inicio__month = 9).count
    ingresos_septiembre = Socio.objects.filter(inicio__month = 9).aggregate(Sum('cuota'))
    septiembre= ingresos_septiembre['cuota__sum']
    
    #registrados mes de octubre
    registro_octubre = Socio.objects.filter(inicio__month = 10).count
    ingresos_octubre = Socio.objects.filter(inicio__month = 10).aggregate(Sum('cuota'))
    octubre= ingresos_octubre['cuota__sum']
    
    #registrados mes de noviembre
    registro_noviembre = Socio.objects.filter(inicio__month = 11).count
    ingresos_noviembre = Socio.objects.filter(inicio__month = 11).aggregate(Sum('cuota'))
    noviembre= ingresos_noviembre['cuota__sum']
    
    #registrados mes de diciembre
    registro_diciembre = Socio.objects.filter(inicio__month = 12).count
    ingresos_diciembre = Socio.objects.filter(inicio__month = 12).aggregate(Sum('cuota'))
    diciembre= ingresos_diciembre['cuota__sum']
    
    #-----------INGRESO MENSUAL $$-----------#    
    ingreso_mens = Socio.objects.filter(estado="Activo").aggregate(Sum("cuota"))
    ingreso_mensual = ingreso_mens['cuota__sum']
    
    
    #-----------REGISTRO ANUAL DE SOCIOS-----------#    
    
    registros_anual = Socio.objects.filter(registro__year=2022).count    

    
    #-----------INGRESO ANUAL $$-----------#    
    
    ingreso_anual= Socio.objects.filter(inicio__year = 2022).aggregate(Sum('cuota'))
    anual = ingreso_anual['cuota__sum']
    
    
    
    return render(request, 'dashboard/estadisticas.html', 
                  {'registro_diario': registro_diario, 'registro_mensual': registro_mensual,
                   'activos': activos, 'no_activos':no_activos, 
                   'ingreso_mensual': ingreso_mensual, 'registro_junio': registro_junio, 'junio': junio,
                   'registro_julio':registro_julio, 'julio' : julio,
                   'registro_agosto': registro_agosto,'agosto' : agosto, 
                   'registro_septiembre' : registro_septiembre,'septiembre': septiembre,  
                   'registro_octubre' : registro_octubre,'octubre': octubre, 
                   'registro_noviembre': registro_noviembre,'noviembre': noviembre,  
                   'registro_diciembre':registro_diciembre, 'diciembre': diciembre,
                   'registros_anual': registros_anual,
                   'anual': anual, 'fecha_hoy': fecha_hoy})
                

#-------------VISTA SOCIOS NO ACTIVOS---------------#

def socios_no_activos(request):
    """
    Funcion actualiza los activos a no activos al terminar su mes de membresia.
    """
    hoy = date.today()
    vencido = Socio.objects.filter(vencimiento__lte = hoy)
    
    print(vencido)
    #lista_vencidos= []
    with transaction.atomic():    
        for key in vencido:
            print(key)
            Socio.objects.filter(vencimiento__lte = hoy).update(estado = 'No activo', aldia= 'NO', cuota = 0000.00)
    paginator = Paginator(vencido, 8) # 8 socios no activos en cada pagina
    page = request.GET.get('page')
    pagina_actual = paginator.get_page(page)
    return render(request, 'dashboard/socios_no_activos.html', {'vencido': pagina_actual, 'hoy': hoy} )

