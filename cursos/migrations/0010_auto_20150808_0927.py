# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0009_curso_realizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adulto',
            name='distrito',
            field=models.ForeignKey(default=None, blank=True, to='cursos.Distrito', null=True),
        ),
        migrations.AlterField(
            model_name='adulto',
            name='grupo',
            field=models.ForeignKey(default=None, blank=True, to='cursos.Grupo', null=True),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='pago',
            field=models.CharField(max_length=1, verbose_name=b'Forma de pago', choices=[(b'1', b'Deposito'), (b'2', b'Transferencia')]),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='referencia',
            field=models.CharField(default=None, max_length=20, verbose_name=b'Referencia del Pago'),
        ),
    ]
