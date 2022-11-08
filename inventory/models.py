from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class equipo(models.Model):
    MARCA = models.CharField(max_length=40)
    MODELO = models.CharField(max_length=40)
    TIPO_EQUIPO = models.CharField(max_length=40)
    NO_SERIE = models.CharField(max_length=40)
    TIPO_DD = models.CharField(max_length=40, blank=True)
    ESPACIO_DD = models.BigIntegerField()
    RAM = models.CharField(max_length=5, blank=True)
    T_RAM = models.CharField(max_length=5, blank=True)
    SYS_OP = models.CharField(max_length=30, blank=True)
    MAC = models.CharField(max_length=20, blank=True)
    IP = models.CharField(max_length=17, blank=True)
    TEAMVIEWER = models.CharField(max_length=11, blank=True)
    ANYDESK = models.CharField(max_length=12, blank=True)
    CREATEDAT = models.DateTimeField(auto_now_add=True, blank=True)
    DESCRIPTION = models.TextField(blank=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.MARCA