"""Tables for templates_interface."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_templates_interface import models

class Dot1qTemplateTable(BaseTable):
    """Table for Dot1qTemplate."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.Dot1qTemplate,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.Dot1qTemplate
        fields = ('pk', 'name', 'key', 'description', 'mode', 'dot1q_untagged', 'dot1q_tagged')
