from django.forms import ModelForm
from .models import equipo

class ItemForm(ModelForm):
    class Meta:
        model = equipo
        fields = [
            'MARCA', 
            'MODELO',
            'TIPO_EQUIPO',
            'NO_SERIE',
            'TIPO_DD',
            'ESPACIO_DD',
            'RAM',
            'T_RAM',
            'SYS_OP',
            'MAC',
            'IP',
            'TEAMVIEWER',
            'ANYDESK',    
        ]