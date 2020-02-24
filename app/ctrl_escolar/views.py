from rest_framework.response import Response
from app.ctrl_escolar.serializers import AsistenciaSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from app.ctrl_escolar.models import Asistencia
from django.views.generic import TemplateView

from app.ctrl_escolar.models import Alumno
from datetime import datetime, time, timedelta, date

class CtrAsistenciaCreateList(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer 

    
    def create(self, request, *args, **kwargs):

        id_user=request.data["asis_user"]
        alumno = Alumno.objects.get(id=id_user)

        ahora = datetime.now()
        ahora = time(ahora.hour, ahora.minute, ahora.second)
        
        entrada_inicial = alumno.al_entrada_init
        entrada_tolerancia = alumno.al_entrada_end
        salida_inicial = alumno.al_salida_init
        salida_final = alumno.al_dalida_end

        # dato=datetime.combine(date.today(), entrada) - datetime.combine(date.today(), ahora)
        # print(dato)

        if ahora <= entrada_inicial:
            request.data["asis_tipo_evento"]="1" 
            request.data["asis_tipo_tiempo"]="1"
        elif ahora <= entrada_tolerancia:
            request.data["asis_tipo_evento"]="1" 
            request.data["asis_tipo_tiempo"]="2"
        elif ahora < salida_inicial:
            request.data["asis_tipo_evento"]="2" 
            request.data["asis_tipo_tiempo"]="4"
        elif ahora <= salida_final:
            request.data["asis_tipo_evento"]="2" 
            request.data["asis_tipo_tiempo"]="1"
        else:
            request.data["asis_tipo_evento"]="2" 
            request.data["asis_tipo_tiempo"]="3"
        
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    

class vistaprueba(TemplateView):
    template_name = "contenido.html"


