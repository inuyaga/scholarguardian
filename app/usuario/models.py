from django.db import models
from django.contrib.auth.models import AbstractUser
from app.ctrl_escolar.models import Colegio
# Create your models here.
class User(AbstractUser):
    foto_perfil=models.ImageField('Foto Perfil', upload_to='foto_perfil/')
    fecha_nacimiento=models.DateField('Fecha de nacimiento',null=True, blank=True)
    telefono=models.BigIntegerField('Telefono', null=True, blank=True)
    TIPO_USUARIO=((1, 'BASICO'), (2, 'AVANZADO'))
    tipo_user=models.IntegerField('Tipo de usuario', choices=TIPO_USUARIO, default=1)
    
    class Meta:
        db_table = 'auth_user' 


class Alumno(models.Model):
    al_nombres=models.CharField('Nombre alumno',max_length=100)
    al_apellidos=models.CharField('Apellidos',max_length=100)
    al_foto=models.ImageField("Foto estuduante", upload_to="img/foto/estuduantes/",  null=True, blank=True)
    al_correo=models.EmailField('Correo')
    al_tutor=models.ForeignKey(User,verbose_name='Tutor de alumno', on_delete=models.CASCADE, null=True, blank=True)
    al_colegio=models.ForeignKey(Colegio,verbose_name='Colegio al que pertenece', on_delete=models.CASCADE, null=True, blank=True)
    al_huella=models.CharField("Huella digital", max_length=700,  null=True, blank=True)
    al_entrada_init=models.TimeField("Configuracion entrada inicial",  null=True, blank=True)
    al_entrada_end=models.TimeField("Tolerancia entrada",  null=True, blank=True)
    
    al_salida_init=models.TimeField("Configuracion salida inicial",  null=True, blank=True)
    al_dalida_end=models.TimeField("Tolerancia salida",  null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.al_nombres, self.al_apellidos)