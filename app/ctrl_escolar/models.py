from django.db import models
from app.usuario.models import User
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


class Alumno(models.Model):
    al_nombres=models.CharField('Nombre alumno',max_length=100)
    al_apellidos=models.CharField('Apellidos',max_length=100)
    al_foto=models.ImageField("Foto estuduante", upload_to="img/foto/estuduantes/",  null=True, blank=True)
    al_correo=models.EmailField('Correo')
    al_tutor=models.ForeignKey(User,verbose_name='Tutor de alumno', on_delete=models.CASCADE, null=True, blank=True)
    al_colegio=models.ForeignKey(Colegio,verbose_name='Colegio al que pertenece', on_delete=models.CASCADE, null=True, blank=True)
    al_huella=models.BinaryField("Huella digital", null=True, blank=True)
    al_entrada_init=models.TimeField("Configuracion entrada inicial",  null=True, blank=True)
    al_entrada_end=models.TimeField("Tolerancia entrada",  null=True, blank=True)
    
    al_salida_init=models.TimeField("Configuracion salida inicial",  null=True, blank=True)
    al_dalida_end=models.TimeField("Tolerancia salida",  null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.al_nombres, self.al_apellidos)



class Asistencia(models.Model):
    asis_user=models.ForeignKey(Alumno, verbose_name='Alumno', on_delete=models.CASCADE)
    asis_hra_evento=models.DateTimeField('Fecha y hora registrada', auto_now_add=True)
    TIPO_EVENTO=((1, 'Entrada'), (2, 'Salida'))
    asis_tipo_evento=models.IntegerField('Tipo de evento', choices=TIPO_EVENTO)
    TIPO_TIEMPO=((1, 'A tiempo'), (2, 'Tolerancia'), (3, 'Fuera de rango de horario'), (4, 'Antes de tiempo'))
    asis_tipo_tiempo=models.IntegerField('Tipo de tiempo', choices=TIPO_TIEMPO)

    def __str__(self):
        return str(self.asis_user)
