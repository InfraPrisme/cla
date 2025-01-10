"""API serializers for nautobot_templates_interface."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

"""Define the class to add the model Dot1q Template into the API"""
class Dot1qTemplateSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):
    """Dot1qTemplate Serializer."""
    class Meta:
        """Meta attributes."""

        model = models.Dot1qTemplate
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []