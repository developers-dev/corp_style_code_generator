# @dn- Ui_Component Module
from typing import Any, Dict, List, Optional


class DN_UIComponent:
    def __init__(self, dn_id: str, dn_type: str, dn_props: Dict[str, Any]) -> None:
        """
        Initialize a ui component with id, type and properties.
        """
        self.dn_id = dn_id
        self.dn_type = dn_type
        self.dn_props = dn_props

    def dn_render(self) -> str:
        """
        Render the ui component as a string.
        """
        return f"<{self.dn_type} id='{self.dn_id}' {self.dn_format_props()}>"

    def dn_format_props(self) -> str:
        """
        Format properties as a string.
        """
        return ' '.join([f"{k}='{v}'" for k, v in self.dn_props.items()])


def dn_create_component(dn_id: str, dn_type: str, dn_props: Dict[str, Any]) -> DN_UIComponent:
    """
    Create a ui component.
    """
    return DN_UIComponent(dn_id, dn_type, dn_props)


def dn_render_components(dn_components: List[DN_UIComponent]) -> str:
    """
    Render a list of ui components as a string.
    """
    return '\n'.join([component.dn_render() for component in dn_components])


def dn_add_prop(component: DN_UIComponent, prop_name: str, prop_value: Any) -> None:
    """
    Add a property to a ui component.
    """
    if prop_name in component.dn_props:
        raise ValueError(f"Property '{prop_name}' already exists in component '{component.dn_id}'")
    component.dn_props[prop_name] = prop_value


def dn_remove_prop(component: DN_UIComponent, prop_name: str) -> None:
    """
    Remove a property from a ui component.
    """
    if prop_name not in component.dn_props:
        raise ValueError(f"Property '{prop_name}' does not exist in component '{component.dn_id}'")
    del component.dn_props[prop_name]


def dn_update_prop(component: DN_UIComponent, prop_name: str, prop_value: Any) -> None:
    """
    Update a property in a ui component.
    """
    if prop_name not in component.dn_props:
        raise ValueError(f"Property '{prop_name}' does not exist in component '{component.dn_id}'")
    component.dn_props[prop_name] = prop_value