from rest_framework import serializers
from app.ctrl_escolar.models import Asistencia, Alumno
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
   


