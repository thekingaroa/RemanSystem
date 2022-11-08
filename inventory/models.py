from django.db import models
from django.contrib.auth.models import User
from .choices import RAZONES_SOCIALES, SYSOP, T_EQUIPO, TERMINALES, TIPO_DDISCO, TIPO_RAM, UBICACIONES

# Create your models here.
class Unidades(models.Model):
    NOMBRE = models.CharField(max_length = 40)
    TERMINAL = models.CharField(max_length = 2, choices=TERMINALES)
    UBICACION = models.CharField(max_length = 30, choices=UBICACIONES)
    
    def __str__(self) -> str:
        return self.NOMBRE

class equipo(models.Model):
    MARCA = models.CharField(max_length=40)
    MODELO = models.CharField(max_length=40)
    TIPO_DE_EQUIPO = models.CharField(max_length=40, choices=T_EQUIPO)
    NUMERO_DE_SERIE = models.CharField(max_length=40)
    TIPO_DE_DISCO = models.CharField(max_length=40, choices=TIPO_DDISCO)
    ESPACIO_EN_DISCO = models.BigIntegerField()
    RAM = models.CharField(max_length=5, blank=True)
    TIPO_DE_RAM = models.CharField(max_length=5, choices=TIPO_RAM)
    SISTEMA_OPERATIVO = models.CharField(max_length=30, choices=SYSOP)
    MAC = models.CharField(max_length=20, blank=True)
    #IP = models.CharField(max_length=17, blank=True)
    IP = models.GenericIPAddressField()
    TEAMVIEWER_ID = models.CharField(max_length=11, blank=True)
    ANYDESK_ID = models.CharField(max_length=12, blank=True)
    DESCRIPCION = models.TextField(blank=True)
    UNIDAD = models.ForeignKey(Unidades, on_delete=models.SET_DEFAULT, default=None, null=True)
    CREATEDAT = models.DateTimeField(auto_now_add=True, blank=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.MARCA

