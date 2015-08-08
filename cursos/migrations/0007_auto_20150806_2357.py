# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_auto_20150806_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='nomenclatura',
            field=models.CharField(max_length=8, verbose_name=b'Nomenclatura del tipo de curso para Nivel Intermedio de Institucionales es NII'),
        ),
    ]
