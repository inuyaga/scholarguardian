from django.db import models
from app.usuario.models import Alumno
# Create your models here.
class Asistencia(models.Model):
    asis_user=models.ForeignKey(Alumno, verbose_name='Alumno', on_delete=models.CASCADE)
    asis_hra_evento=models.DateTimeField('Fecha y hora registrada', auto_now_add=True)
    TIPO_EVENTO=((1, 'ENTRADA'), (2, 'SALIDA'))
    asis_tipo_evento=models.IntegerField('Tipo de evento', choices=TIPO_EVENTO)
    TIPO_TIEMPO=((1, 'A tiempo'), (2, 'Tolerancia'), (3, 'Retardo'))
    asis_tipo_tiempo=models.IntegerField('Tipo de tiempo', choices=TIPO_TIEMPO)
