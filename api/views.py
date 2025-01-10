from rest_framework.viewsets import ModelViewSet

from nautobot_templates_interface.models import Dot1qTemplate
from .serializers import Dot1qTemplateSerializer

class Dot1qTemplateViewSet(ModelViewSet):
    """API viewset for interacting with Interface Template objects."""

    queryset = Dot1qTemplate.objects.all()
    serializer_class = Dot1qTemplateSerializer