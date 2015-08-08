# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adulto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.IntegerField()),
                ('especial', models.TextField(default=None, verbose_name=b'Impedimiento Fisico o Dieta Especial')),
                ('telefono', models.CharField(default=None, max_length=11)),
                ('correo', models.EmailField(max_length=254)),
                ('cargo_id', models.ForeignKey(to='cursos.Cargo', null=True)),
                ('distrito_id', models.ForeignKey(to='cursos.Distrito', null=True)),
                ('grupo_id', models.ForeignKey(to='cursos.Grupo', null=True)),
                ('region_id', models.ForeignKey(to='cursos.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(default=None, max_length=20, verbose_name=b'Referencia de la forma de pago')),
                ('aprobado', models.BooleanField(default=False)),
                ('certificado', models.CharField(default=None, max_length=3)),
                ('pago', models.CharField(max_length=1, verbose_name=b'Forma de pago', choices=[(b'Deposito', 1), (b'Transferencia', 1)])),
                ('adulto_id', models.ForeignKey(to='cursos.Adulto')),
                ('curso_id', models.ForeignKey(to='cursos.Curso')),
            ],
        ),
        migrations.RemoveField(
            model_name='adultos',
            name='cargo_id',
        ),
        migrations.RemoveField(
            model_name='adultos',
            name='distrito_id',
        ),
        migrations.RemoveField(
            model_name='adultos',
            name='grupo_id',
        ),
        migrations.RemoveField(
            model_name='adultos',
            name='region_id',
        ),
        migrations.RemoveField(
            model_name='inscritos',
            name='adulto_id',
        ),
        migrations.RemoveField(
            model_name='inscritos',
            name='curso_id',
        ),
        migrations.DeleteModel(
            name='Adultos',
        ),
        migrations.DeleteModel(
            name='Inscritos',
        ),
    ]
