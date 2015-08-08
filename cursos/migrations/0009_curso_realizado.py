# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_auto_20150807_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='realizado',
            field=models.BooleanField(default=False),
        ),
    ]
