from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    foto_perfil=models.ImageField('Foto Perfil', upload_to='foto_perfil/')
    fecha_nacimiento=models.DateField('Fecha de nacimiento',null=True, blank=True)
    telefono=models.BigIntegerField('Telefono', null=True, blank=True)
    TIPO_USUARIO=((1, 'BASICO'), (2, 'AVANZADO'), (3, 'ADMINISTRADOR'))
    tipo_user=models.IntegerField('Tipo de usuario', choices=TIPO_USUARIO)
    # acerca_de_mi=models.CharField('Acerca de mi', max_length=1000, default='.....')
    class Meta:
        db_table = 'auth_user' 


class Alumno(models.Model):
    al_nombres=models.CharField('Nombre alumno',max_length=100)
    al_apellidos=models.CharField('Apellidos',max_length=100)
    al_correo=models.EmailField('Correo')
    al_tutor=models.ForeignKey(User,verbose_name='Tutor de alumno', on_delete=models.CASCADE, null=True, blank=True)