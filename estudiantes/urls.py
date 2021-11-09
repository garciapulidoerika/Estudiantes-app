from rest_framework.routers import DefaultRouter
from estudiantes.views import EstudianteViewSet

router = DefaultRouter()
router.register('estudiantes', EstudianteViewSet)

urlpatterns = router.urls
