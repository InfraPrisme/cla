"""Views for nautobot_templates_interface."""
from nautobot.apps.views import NautobotUIViewSet

from nautobot_templates_interface import filters, forms, models, tables
from nautobot_templates_interface.api import serializers

class Dot1qTemplateUIViewSet(NautobotUIViewSet):
    """ViewSet for Dot1qTemplate views."""

    bulk_update_form_class = forms.Dot1qTemplateBulkEditForm
    filterset_class = filters.Dot1qTemplateFilterSet
    filterset_form_class = forms.Dot1qTemplateFilterForm
    form_class = forms.Dot1qTemplateForm
    lookup_field = "pk"
    queryset = models.Dot1qTemplate.objects.all()
    table_class = tables.Dot1qTemplateTable
    serializer_class = serializers.Dot1qTemplateSerializer
    template_name = "nautobot_templates_interface/dot1qtemplate_create.html"

"""class Dot1qTemplateDetailView(NautobotUIViewSet):
    queryset = models.Dot1qTemplate.objects.all()
    template_name = "nautobot_templates_interface/dot1q_template_detail.html"
    context_object_name = "dot1q_template"
"""