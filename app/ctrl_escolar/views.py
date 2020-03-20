from rest_framework.response import Response
from app.ctrl_escolar.serializers import (
    AsistenciaSerializer, 
    UserRegisterSerializer, 
    AlumnoSerializer, 
    GetHistoryEventAlumnSerializer,
    AlumnoChildSerializer
    )
import base64
from PIL import Image
import io
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework import status, viewsets
from django.views.generic import TemplateView


from app.ctrl_escolar.models import Alumno, Asistencia
from app.usuario.models import User
from datetime import datetime, time, timedelta, date
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from django.core import serializers

from django.utils.formats import localize
class RegisterUser(generics.CreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = UserRegisterSerializer

    # def create(self, request, *args, **kewargs)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class CtrAsistenciaCreateList(viewsets.ModelViewSet):
    queryset = User.objects.all()
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




class LoginAppScholar(APIView):
    def post(self, request):
        bdy = request.body
        print(bdy)
        content = {
            'message': 'Hello, World!',
            'contenido':bdy
            }
        return Response(content)

    def get(self, request):
        content = {
            'message': 'Hello, World!',
            }
        return Response(content)


class GetUserInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # def post(self, request):
    #     bdy = request.body
    #     print(bdy)
    #     content = {
    #         'message': 'Hello, World!',
    #         'contenido':bdy
    #         }
    #     return Response(content)
    

    
    def get(self, request):
        user = User.objects.get(username=request.user)
        photo = user.foto_perfil.url  if  user.foto_perfil != "" else "no"
        content = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'foto_perfil': photo,
            'email': user.email,
            'fecha_nacimiento': localize(user.fecha_nacimiento),
            'telefono': str(user.telefono),
            }
        return Response(content)



class GetHijoUser(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(al_tutor=self.request.user)
        return queryset

class AddAlumnoHijo(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    serializer_class = AlumnoChildSerializer
    queryset = Alumno.objects.all()
    def create(self, request, *args, **kwargs):
        from django.core.files.base import ContentFile
        from base64 import b64decode
        request.data._mutable = True

        image_data = b64decode(request.data['al_foto'])

        request.data['al_entrada_init']=datetime.strptime(request.data['al_entrada_init'], '%Y-%m-%d %H:%M:%S.%f').time()
        request.data['al_entrada_end']=datetime.strptime(request.data['al_entrada_end'], '%Y-%m-%d %H:%M:%S.%f').time()
        request.data['al_salida_init']=datetime.strptime(request.data['al_salida_init'], '%Y-%m-%d %H:%M:%S.%f').time()
        request.data['al_dalida_end']=datetime.strptime(request.data['al_dalida_end'], '%Y-%m-%d %H:%M:%S.%f').time()
        request.data['al_tutor']=request.user.id
        request.data['al_foto']=ContentFile(image_data, 'whatup.png')
        


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetHistoryEventAlumn(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = Asistencia.objects.all()
    serializer_class = GetHistoryEventAlumnSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(asis_user__al_tutor=self.request.user).order_by('-id')
        return queryset 


   


