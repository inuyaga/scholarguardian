from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.ctrl_escolar import views as ctr_view

router = routers.DefaultRouter()
router.register('asist', ctr_view.CtrAsistenciaCreateList)
# urlpatterns = [
#     path('asist/', ctr_view.CtrAsistenciaCreateList.as_view({'get': 'list'})),
# ]
urlpatterns = router.urls