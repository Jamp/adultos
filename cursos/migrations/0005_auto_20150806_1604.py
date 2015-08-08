# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_auto_20150806_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adulto',
            old_name='cargo_id',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='adulto',
            old_name='distrito_id',
            new_name='distrito',
        ),
        migrations.RenameField(
            model_name='adulto',
            old_name='grupo_id',
            new_name='grupo',
        ),
        migrations.RenameField(
            model_name='adulto',
            old_name='region_id',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='region_id',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='tipo_id',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='distrito',
            old_name='region_id',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='distrito_id',
            new_name='distrito',
        ),
        migrations.RenameField(
            model_name='inscrito',
            old_name='adulto_id',
            new_name='adulto',
        ),
        migrations.RenameField(
            model_name='inscrito',
            old_name='curso_id',
            new_name='curso',
        ),
    ]
