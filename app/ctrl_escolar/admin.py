from django.contrib import admin
from app.usuario.models import User
# Register your models here.
from app.ctrl_escolar.models import Alumno, Asistencia

class AsistenciaConfig(admin.ModelAdmin):
    list_display = [
        'asis_user',
        'asis_hra_evento',
        'asis_tipo_evento',
        'asis_tipo_tiempo',
    ]
admin.site.register(Alumno)
admin.site.register(User)
admin.site.register(Asistencia, AsistenciaConfig)