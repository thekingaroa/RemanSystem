from django.forms import ModelForm
from .models import equipo

class ItemForm(ModelForm):
    class Meta:
        model = equipo
        fields = [
            'MARCA', 
            'MODELO',
            'TIPO_DE_EQUIPO',
            'NUMERO_DE_SERIE',
            'TIPO_DE_DISCO',
            'ESPACIO_EN_DISCO',
            'RAM',
            'TIPO_DE_RAM',
            'SISTEMA_OPERATIVO',
            'MAC',
            'IP',
            'TEAMVIEWER_ID',
            'ANYDESK_ID', 
            'DESCRIPCION'   
        ]
  