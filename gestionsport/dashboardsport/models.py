
from datetime import datetime, date, tzinfo

from tabnanny import verbose
from django.db import models
from django.forms import DateField, Textarea

from pytz import timezone


# Create your models here.
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, null=False, verbose_name='Apellido')
    edad = models.IntegerField(null=False, verbose_name='Edad')
    telefono = models.IntegerField(null=False, verbose_name='Telefono')
    telefono_emergencia = models.IntegerField(null=False, verbose_name='Telefono de Emergencia')
    email = models.EmailField(max_length=30, null=True, verbose_name='Email')
    Fecha_Comienzo = models.DateTimeField()
    sueldo = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = 'Profesores'
        ordering = ['id']
        
class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    telefono_emergencia = models.CharField(max_length=20, verbose_name='Tel-emerg')
    email = models.EmailField(max_length=50, null=True, blank=True)
    registro = models.DateTimeField(auto_now=True) #OBSERVAR COMPORTAMIENTOS DEL DATEFIELD
    inicio = models.DateField(null=True, blank=True) 
    vencimiento = models.DateField(null=True, blank=True)
    cuota=models.DecimalField(default=1900.00 ,verbose_name='Cuota', max_digits=6, decimal_places=2)
    pago = (
                    ('No', 'NO'),
                    ('Si', 'SI'),
                    )
                    
    aldia = models.CharField(max_length=17, choices=pago, verbose_name='Cuota al dia?', default='no')
    condicion = (
                    ('No activo', 'No activo'),
                    ('Activo', 'Activo'),
                    )
    estado = models.CharField(max_length=10, verbose_name='Estado', choices=condicion, default='No activo')
    
    
    genero = models.CharField(max_length=30, null=True, blank=True, default='femenino')
    
    
    
    def __str__(self):
        return "{} ({}) ({})".format(self.id, self.nombre, self.genero)
    
    class Meta:
        db_table = 'socio'
        verbose_name = "Socio"
        verbose_name_plural = 'Socios'
        ordering = ['id']


    

