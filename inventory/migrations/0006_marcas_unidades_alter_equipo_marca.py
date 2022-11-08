# Generated by Django 4.1.3 on 2022-11-08 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_equipo_sys_op_alter_equipo_tipo_dd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MARCA', models.CharField(max_length=50)),
                ('RAZON_SOCIAL', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UNIDAD', models.CharField(max_length=50)),
                ('UBICACION', models.CharField(blank=True, max_length=50)),
                ('MARCA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.marcas')),
            ],
        ),
        migrations.AlterField(
            model_name='equipo',
            name='MARCA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.marcas'),
        ),
    ]
