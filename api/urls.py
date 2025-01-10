# api/urls.py
from rest_framework import routers

from .views import InterfaceFeatureViewSet, InterfaceTemplateViewSet, Dot1qTemplateViewSet

router = routers.DefaultRouter()
router.register('dot1qtemplate', Dot1qTemplateViewSet)

urlpatterns = router.urls