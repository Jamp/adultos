from django.contrib import admin
from models import Region, Distrito, Grupo, Cargo, Tipo, Curso, Adulto, Inscrito

class RegionesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class DistritosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    list_filter = ('region',)
    search_fields = ['region']

class GruposAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'distrito')

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class AdultoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'lugar', 'telefono', 'correo', 'atencion')

    def nombre(self, obj):
        return u'%s %s' % (obj.nombres, obj.apellidos)

    def lugar(self, obj):
        estructura = u''

        if obj.grupo:
            estructura += u'%s < ' % obj.grupo.nombre

        if obj.distrito:
            estructura += u'%s < ' % obj.distrito.nombre

        if obj.region:
            estructura += u'%s' % obj.region.nombre

        return estructura

    def atencion(self, obj):
        return obj.especial


class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nomenclatura')


class CursoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'region', 'fecha', 'maximo')

class InscritoAdmin(admin.ModelAdmin):
    list_display = ('adulto', 'curso', 'pago', 'referencia', 'aprobado')


admin.site.register(Region, RegionesAdmin)
admin.site.register(Distrito, DistritosAdmin)
admin.site.register(Grupo, GruposAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Adulto, AdultoAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Inscrito, InscritoAdmin)
