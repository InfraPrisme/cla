"""Models for Templates Interface."""

# Django imports
from django.db import models

# Nautobot imports
from nautobot.apps.models import PrimaryModel, extras_features
from nautobot.core.models.fields import AutoSlugField, slugify_dashes_to_underscores
from nautobot.dcim.choices import InterfaceModeChoices

@extras_features("custom_fields", "custom_validators", "relationships", "graphql")
class Dot1qTemplate(PrimaryModel):
    """Base model for Interface Features."""
    CHARFIELD_MAX_LENGTH = 60
    
    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH, unique=True)
    key = AutoSlugField(
        blank=True,
        max_length=CHARFIELD_MAX_LENGTH,
        separator="_",
        populate_from="label",
        help_text="Internal field name. Please use underscores rather than dashes in this key.",
        slugify_function=slugify_dashes_to_underscores,
        unique=True,
    )
    description = models.CharField(max_length=200, blank=True)

    # Champ pour sélectionner le mode de configuration 802.1q
    mode = models.CharField(max_length=50, choices=InterfaceModeChoices, blank=True)

    # Champs hérités du code de la classe "Interface" native
    dot1q_untagged = models.ForeignKey(
        to="ipam.VLAN",
        on_delete=models.SET_NULL,
        related_name="dot1q_template_untagged_vlans",
        null=True,
        blank=True,
        verbose_name="Untagged VLAN",
    )

    # Champs hérités du code de la classe "Interface" native
    dot1q_tagged = models.ManyToManyField(
        to="ipam.VLAN",
        related_name="dot1q_template_tagged_vlans",
        blank=True,
        verbose_name="Tagged VLANs",
    )

    class Meta:
        """Meta class."""
        ordering = ["name"]

    def clean(self):
        super().clean()

    def __str__(self):
        return self.name
