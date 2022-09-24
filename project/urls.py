from rest_framework import routers  
from .api import ProjectViewSet

router = routers.DefaultRouter() # rutas basicas (CRUD) que nos provee DRF

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls


