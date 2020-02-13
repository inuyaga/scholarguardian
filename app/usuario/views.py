from rest_framework import generics
from app.usuario.serializers import UserSerializer
from app.usuario.models import User 

class UsuarioList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer