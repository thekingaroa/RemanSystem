# Generated by Django 4.1.3 on 2022-11-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_marcas_unidades_alter_equipo_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidades',
            name='MARCA',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='MARCA',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='Marcas',
        ),
        migrations.DeleteModel(
            name='Unidades',
        ),
    ]
