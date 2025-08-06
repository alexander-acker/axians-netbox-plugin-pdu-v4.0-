from netbox.plugins import PluginMenuButton, PluginMenuItem

import_icon_class = "mdi mdi-upload"

menu_items = (
    PluginMenuItem(
        link="plugins:axians_netbox_pdu:pduconfig_list",
        link_text="PDU Config",
        permissions=["axians_netbox_pdu.view_pduconfig"],
        buttons=(
            PluginMenuButton(
                link="plugins:axians_netbox_pdu:pduconfig_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                permissions=["axians_netbox_pdu.add_pduconfig"],
            ),
            PluginMenuButton(
                link="plugins:axians_netbox_pdu:pduconfig_import",
                title="Bulk Add",
                icon_class=import_icon_class,
                permissions=["axians_netbox_pdu.add_pduconfig"],
            ),
        ),
    ),
)
