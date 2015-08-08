# -*- coding: utf-8 -*-
from django.db import models


class Region(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombre


class Distrito(models.Model):
    nombre = models.CharField(max_length=20)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.nombre



class Grupo(models.Model):
    nombre = models.CharField(max_length=20)
    distrito = models.ForeignKey(Distrito)

    def __unicode__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField('Curso', max_length=50)
    nomenclatura = models.CharField('Nomenclatura', max_length=8)

    def __unicode__(self):
        return self.nombre


class Curso(models.Model):
    tipo = models.ForeignKey(Tipo)
    region = models.ForeignKey(Region)
    fecha = models.DateField('Fecha de la realización del curso')
    maximo = models.PositiveSmallIntegerField('Máximo de Personas a Inscribir')
    realizado = models.BooleanField(default=False)
    creado_at = models.DateTimeField(auto_now_add=True)
    modicado_in = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.tipo.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Adulto(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.PositiveIntegerField()
    cargo = models.ForeignKey(Cargo)
    grupo = models.ForeignKey(Grupo, blank=True, null=True, default=None)
    distrito = models.ForeignKey(Distrito, blank=True, null=True, default=None)
    region = models.ForeignKey(Region)
    especial = models.TextField('Impedimiento Fisico o Dieta Especial', default=None)
    telefono = models.CharField(max_length=11, default=None)
    correo = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.nombres, self.apellidos)


class Inscrito(models.Model):
    adulto = models.ForeignKey(Adulto)
    curso = models.ForeignKey(Curso)
    referencia = models.CharField('Referencia del Pago', max_length=20, default=None)
    aprobado = models.BooleanField(default=False)
    certificado = models.CharField('Número de Certificado', max_length=3, default=None)
    enviado = models.BooleanField('Enviado por correo', default=False)

    formaPago = (
        ('1', 'Deposito'),
        ('2', 'Transferencia'),
    )
    pago = models.CharField('Forma de pago', max_length=1, choices=formaPago)
