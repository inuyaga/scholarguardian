from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    foto_perfil=models.ImageField('Foto Perfil', upload_to='foto_perfil/')
    fecha_nacimiento=models.DateField('Fecha de nacimiento',null=True, blank=True)
    telefono=models.BigIntegerField('Telefono', null=True, blank=True)
    TIPO_USUARIO=((1, 'BASICO'), (2, 'AVANZADO'))
    tipo_user=models.IntegerField('Tipo de usuario', choices=TIPO_USUARIO, default=1)
    class Meta:
        db_table = 'auth_user' 


