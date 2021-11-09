from rest_framework.routers import DefaultRouter
from clase.views import ClaseViewSet

router = DefaultRouter()
router.register('clase', ClaseViewSet)

urlpatterns = router.urls