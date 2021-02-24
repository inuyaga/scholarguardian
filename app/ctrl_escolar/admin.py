from django.contrib import admin
from app.usuario.models import User
# Register your models here.
from app.ctrl_escolar.models import Alumno, Asistencia, Colegio

class AsistenciaConfig(admin.ModelAdmin):
    list_display = [
        'asis_user',
        'asis_hra_evento',
        'asis_tipo_evento',
        'asis_tipo_tiempo',
    ]
class ColegioConfig(admin.ModelAdmin):
    list_display = [
        'col_nombre',
        'col_fecha_add',
        'col_direccion',
        'col_logo',
    ]
class AlumnoConfig(admin.ModelAdmin):
    list_display = [
        'al_nombres',
        'al_apellidos',
        'al_correo',
        'al_tutor',
        'al_colegio',
        'al_entrada_init',
        'al_entrada_end',
        'al_salida_init',
        'al_dalida_end',
    ]







admin.site.register(Alumno, AlumnoConfig) 
admin.site.register(Asistencia, AsistenciaConfig)
admin.site.register(Colegio, ColegioConfig)












