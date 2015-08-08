# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adultos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.IntegerField(max_length=9)),
                ('especial', models.TextField(default=None, verbose_name=b'Impedimiento Fisico o Dieta Especial')),
                ('telefono', models.CharField(default=None, max_length=11)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado_at', models.DateField(auto_created=True)),
                ('fecha', models.DateField(verbose_name=b'Fecha de la realizaci\xc3\xb3n del curso')),
                ('modicado_in', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('distrito_id', models.ForeignKey(to='cursos.Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pago', models.CharField(max_length=1, verbose_name=b'Forma de pago(1 deposito, 2 transferencia)')),
                ('referencia', models.CharField(default=None, max_length=20, verbose_name=b'Referencia de la forma de pago')),
                ('aprobado', models.BooleanField(default=False)),
                ('certificado', models.CharField(default=None, max_length=3)),
                ('adulto_id', models.ForeignKey(to='cursos.Adultos')),
                ('curso_id', models.ForeignKey(to='cursos.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('nomenclatura', models.CharField(max_length=5, verbose_name=b'Nomenclatura del tipo de curso para Nivel Intermedio de Institucionales es NII')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='region_id',
            field=models.ForeignKey(to='cursos.Region'),
        ),
        migrations.AddField(
            model_name='curso',
            name='region_id',
            field=models.ForeignKey(to='cursos.Region'),
        ),
        migrations.AddField(
            model_name='curso',
            name='tipo_id',
            field=models.ForeignKey(to='cursos.Tipo'),
        ),
        migrations.AddField(
            model_name='adultos',
            name='cargo_id',
            field=models.ForeignKey(to='cursos.Cargo', null=True),
        ),
        migrations.AddField(
            model_name='adultos',
            name='distrito_id',
            field=models.ForeignKey(to='cursos.Distrito', null=True),
        ),
        migrations.AddField(
            model_name='adultos',
            name='grupo_id',
            field=models.ForeignKey(to='cursos.Grupo', null=True),
        ),
        migrations.AddField(
            model_name='adultos',
            name='region_id',
            field=models.ForeignKey(to='cursos.Region'),
        ),
    ]
