# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_auto_20150806_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='creado_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='maximo',
            field=models.PositiveSmallIntegerField(verbose_name=b'M\xc3\xa1ximo de Personas a Inscribir'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='modicado_in',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='certificado',
            field=models.CharField(default=None, max_length=3, verbose_name=b'N\xc3\xbamero de Certificado'),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='enviado',
            field=models.BooleanField(default=False, verbose_name=b'Enviado por correo'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name=b'Curso'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nomenclatura',
            field=models.CharField(max_length=8, verbose_name=b'Nomenclatura'),
        ),
    ]
