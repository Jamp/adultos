# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_auto_20150806_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='maximo',
            field=models.PositiveSmallIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscrito',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='adulto',
            name='cedula',
            field=models.PositiveIntegerField(),
        ),
    ]
