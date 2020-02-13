from rest_framework import serializers
from app.ctrl_escolar.models import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['id', 'asis_user', 'asis_tipo_evento', 'asis_tipo_tiempo']
        read_only_fields = ('id',)
   
