# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_auto_20150806_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adulto',
            name='cargo_id',
            field=models.ForeignKey(to='cursos.Cargo'),
        ),
        migrations.AlterField(
            model_name='adulto',
            name='distrito_id',
            field=models.ForeignKey(default=None, to='cursos.Distrito', null=True),
        ),
        migrations.AlterField(
            model_name='adulto',
            name='grupo_id',
            field=models.ForeignKey(default=None, to='cursos.Grupo', null=True),
        ),
    ]
