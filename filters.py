"""Filtering for nautobot_templates_interface."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from nautobot_templates_interface import models


class Dot1qTemplateFilterSet(NautobotFilterSet, NameSearchFilterSet):
    """Filter for Dot1qTemplate."""

    class Meta:
        """Meta attributes for filter."""

        model = models.Dot1qTemplate

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "description", "mode", 'dot1q_untagged', 'dot1q_tagged']