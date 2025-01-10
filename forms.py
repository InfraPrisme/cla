"""Forms for nautobot_templates_interface."""
from django import forms
from nautobot.apps.forms import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin, RelationshipModelFormMixin
from nautobot.core.forms import add_blank_choice,SlugField,StaticSelect2
from nautobot.dcim.forms import InterfaceModeChoices
from nautobot_templates_interface import models
from nautobot.ipam.models import VLAN


class Dot1qTemplateForm(NautobotModelForm, RelationshipModelFormMixin):  # Inspiré de la classe "InterfaceForm"
    """Dot1q template creation/edit form."""

    name = forms.CharField(
        required=True, max_length=50, help_text="Name of the field as displayed to users."
    )
    key = SlugField(
        label="Key",
        max_length=50,
        slug_source="name",
        help_text="Internal name of this field. Please use underscores rather than dashes.",
    )
    mode = forms.ChoiceField(
        choices=add_blank_choice(InterfaceModeChoices),
        required=True,
        widget=StaticSelect2(),
        label="802.1Q Mode",
        help_text="""
            Access: One untagged VLAN<br />
            Tagged: One untagged VLAN and/or one or more tagged VLANs<br />
            Tagged (All): Implies all VLANs are available (w/optional untagged VLAN)
            """,
    )
    dot1q_untagged = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False,
        label="Untagged VLAN",
    )
    dot1q_tagged = DynamicModelMultipleChoiceField(
        queryset=VLAN.objects.all(),
        required=False,
        label="Tagged VLANs",
    )

    class Meta:
        """Meta attributes."""
        model = models.Dot1qTemplate
        fields = [
            "name",
            "key",
            "description",
            "mode",
            "dot1q_untagged",
            "dot1q_tagged",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial.get("key"):
            self.fields["key"].disabled = True

    def clean(self):
        super().clean()
      

class Dot1qTemplateBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """Dot1q Template bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.Dot1qTemplate.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""
        nullable_fields = [
            "description",
        ]


class Dot1qTemplateFilterForm(NautobotFilterForm):
    """Dot1q Template filter form to filter searches."""
    model = models.Dot1qTemplate
    field_order = ["name","mode"]
    name = forms.CharField(required=False, label="Name")
    mode = forms.ChoiceField(
        choices=add_blank_choice(InterfaceModeChoices),
        required=False,
        widget=StaticSelect2(),
        label="802.1Q Mode",
    )
