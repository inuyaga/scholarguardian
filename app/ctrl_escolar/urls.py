from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.ctrl_escolar import views as ctr_view
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('asist', ctr_view.CtrAsistenciaCreateList)
app_name = 'ctrl'
urlpatterns = [
    path('app/v1/app/login2/', ctr_view.AutenticacionUser.as_view(), name='login2'), 
    # path('app/v1/app/login/', ctr_view.LoginAppScholar.as_view(), name='login'), 
    path('app/v1/app/register/', ctr_view.RegisterUser.as_view(), name='registro'), 
    path('app/v1/app/get/user/info/', ctr_view.GetUserInfo.as_view(), name='infouser'), 
    path('app/v1/app/get/alumnos/info/', ctr_view.GetHijoUser.as_view(), name='get_alu'), 
    path('app/v1/app/get/alumnos/historia/eventos/', ctr_view.GetHistoryEventAlumn.as_view(), name='history_event'), 
    path('app/v1/app/add/alumnos/', ctr_view.AddAlumnoHijo.as_view(), name='add_al'), 
    path('app/v1/app/colegios/list/', ctr_view.GetColegiosEstudios.as_view(), name='col_list'), 
    path('app/v1/app/user/update/<int:pk>', ctr_view.UsuarioUpdateAppi.as_view(), name='usr_update'), 
]
urlpatterns += router.urls