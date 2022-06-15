


ingreso_mens = Socio.objects.filter(estado="Activo").aggregate(Sum("cuota"))
    ingreso_mensual = ingreso_mens['cuota__sum']
    total_anio = ingreso_mensual
    
    return render(request, 'dashboard/estadisticas.html', 
                  {'registro_mensual': registro_mensual, 'registros_anual': registros_anual, 
                   'activos': activos, 'no_activos':no_activos, 
                   'ingreso_mensual': ingreso_mensual, 'total_anio': total_anio})

ingresos = Socio.objects.filter(estado="Activo").aggregate(Sum("cuota")). 
   
    
    
    