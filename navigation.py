"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab


## Add your app into the APPS GUI Menu
"""
items = (
    NavMenuItem(
        link="plugins:nautobot_templates_interface:interfacetemplates_list",
        name="Templates Interface",
        permissions=["nautobot_templates_interface.view_interfacetemplates"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_templates_interface:interfacetemplates_add",
                permissions=["nautobot_templates_interface.add_interfacetemplates"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Templates Interface", items=tuple(items)),),
    ),
)
"""

## Add your application directly in the nav bar menu
items = (
    NavMenuItem(
        link="plugins:nautobot_templates_interface:interfacetemplate_list",
        name="Interface Templates",
        permissions=["nautobot_templates_interface.view_interfacetemplate"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_templates_interface:interfacetemplate_add",
                permissions=["nautobot_templates_interface.add_interfacetemplate"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:nautobot_templates_interface:interfacefeature_list",
        name="Interface Features",
        permissions=["nautobot_templates_interface.view_interfacefeature"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_templates_interface:interfacefeature_add",
                permissions=["nautobot_templates_interface.add_interfacefeature"],
            ),
        ),
    ),
    NavMenuItem(
        link="plugins:nautobot_templates_interface:dot1qtemplate_list",
        name="802.1q Templates",
        permissions=["nautobot_templates_interface.view_dot1qtemplate"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_templates_interface:dot1qtemplate_add",
                permissions=["nautobot_templates_interface.add_dot1qtemplate"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Templates Interface",
        groups=(NavMenuGroup(name="Templates Interface", items=tuple(items)),),
    ),
)

