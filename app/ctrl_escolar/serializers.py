from rest_framework import serializers
from app.ctrl_escolar.models import Asistencia, Alumno
from app.usuario.models import User
from django.utils.formats import localize

class HoraFormat1n8(serializers.RelatedField):
    def to_representation(self, value):
        hora = localize(value)
        return hora


class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id', 'al_nombres',  'al_apellidos', 'al_correo', 'al_colegio']
        # read_only_fields = ('id',)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',  
            'last_name', 
            'username', 
            'email',
            'password', 
            ]
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class AsistenciaSerializer(serializers.ModelSerializer):

    # retorna solo el id de la relacion 
    # asis_user = serializers.RelatedField(source='Alumno', read_only=True)
    
    # obtine todo el objeto a mostrar en consulta
    asis_user=AlumnoSerializer(read_only=True)
    
    asis_tipo_evento = serializers.CharField(source='get_asis_tipo_evento_display')
    asis_tipo_tiempo = serializers.CharField(source='get_asis_tipo_tiempo_display')
    asis_hra_evento = HoraFormat1n8(read_only=True)
    # retiorna el __str__ del modelo 
    asis_user = serializers.StringRelatedField()
    class Meta:
        model = Asistencia
        fields = ['id',  'asis_user', 'asis_tipo_evento', 'asis_tipo_tiempo', 'asis_hra_evento']
        read_only_fields = ('id',)
   


class AlumnoSerializer(serializers.ModelSerializer):
    al_colegio = serializers.StringRelatedField()
    class Meta:
        model = Alumno
        fields = [
            'id',
            'al_nombres',
            'al_apellidos',
            'al_foto',
            'al_correo',
            'al_colegio',
            'al_entrada_init',
            'al_entrada_end',
            'al_salida_init',
            'al_dalida_end',
        ]

class GetHistoryEventAlumnSerializer(serializers.ModelSerializer):
    # al_colegio = serializers.StringRelatedField()
    asis_tipo_evento = serializers.CharField(source='get_asis_tipo_evento_display')
    asis_tipo_tiempo = serializers.CharField(source='get_asis_tipo_tiempo_display')
    # asis_hra_evento = HoraFormat1n8(read_only=True)
    asis_hra_evento = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    
    asis_user = serializers.StringRelatedField()
    
    class Meta:
        model = Asistencia
        fields = [
            'id',
            'asis_user',
            'asis_hra_evento',
            'asis_tipo_evento',
            'asis_tipo_tiempo',
        ]



