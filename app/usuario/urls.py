from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.usuario import views as VistaUser

urlpatterns = [
    path('frame/', VistaUser.UsuarioList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)