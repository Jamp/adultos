# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20150806_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
