from django.db import models
from app.usuario.models import Alumno, User
# Create your models here.

class Subcripcion(models.Model):
    sub_user=models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE, null=False, blank=False)
    su_fecha_vencimiento=models.DateTimeField("Vencimiento subcripción")


class Colegio(models.Model):
    col_nombre=models.CharField("Nombre de colegio", max_length=200, unique=True)
    col_fecha_add=models.DateField(auto_now_add=True)
    col_direccion=models.CharField("Ubicacion del colegio", max_length=300)
    col_logo=models.ImageField("Logo de institución", upload_to="img/logo/")

    def __str__(self):
        return self.col_nombre

class Asistencia(models.Model):
    asis_user=models.ForeignKey(Alumno, verbose_name='Alumno', on_delete=models.CASCADE)
    asis_hra_evento=models.DateTimeField('Fecha y hora registrada', auto_now_add=True)
    TIPO_EVENTO=((1, 'ENTRADA'), (2, 'SALIDA'))
    asis_tipo_evento=models.IntegerField('Tipo de evento', choices=TIPO_EVENTO)
    TIPO_TIEMPO=((1, 'A tiempo'), (2, 'Tolerancia'), (3, 'Retardo'))
    asis_tipo_tiempo=models.IntegerField('Tipo de tiempo', choices=TIPO_TIEMPO)

    def __str__(self):
        return self.col_nombre
