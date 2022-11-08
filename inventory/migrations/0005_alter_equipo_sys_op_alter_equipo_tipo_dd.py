# Generated by Django 4.1.3 on 2022-11-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_equipo_sys_op_alter_equipo_tipo_equipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='SYS_OP',
            field=models.CharField(choices=[('WINDOWS 8', 'Windows 8'), ('WINDOWS 10 ENTERPRISE', 'Windows 10 Enterprise'), ('WINDOWS 10 PRO', 'Windows 10 Pro'), ('WINDOWS 11 PRO', 'Windows 11 Pro')], max_length=30),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='TIPO_DD',
            field=models.CharField(choices=[('HDD', 'Mecánico'), ('SSD', 'Estado Sólido')], max_length=40),
        ),
    ]
