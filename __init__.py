"""App declaration for nautobot_templates_interface."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig



class TemplatesInterfaceConfig(NautobotAppConfig):
    """App configuration for the nautobot_templates_interface app."""

    name = "nautobot_templates_interface"
    verbose_name = "Templates Interface"
    description = "Application that provides an flexible way to create interface/port template."
    base_url = "templates-interface"
    required_settings = []
    version = 1.0
    default_settings = {}
    caching_config = {}
    searchable_models = ["Dot1qTemplate"]

config = TemplatesInterfaceConfig
