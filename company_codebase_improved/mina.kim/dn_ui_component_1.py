# @dn- Ui_Component Module

from typing import Optional, List

class DN_UIComponent:
    """
    DN_UIComponent is a class for managing UI components.
    """

    def __init__(self, components: Optional[List[str]] = None):
        self.components = components if components else []

    def dn_add_component(self, component: str) -> None:
        """
        Add a new component to the components list.

        :param component: The name of the component.
        """
        self.components.append(component)

    def dn_remove_component(self, component: str) -> None:
        """
        Remove a component from the components list.

        :param component: The name of the component.
        """
        if component in self.components:
            self.components.remove(component)

    def dn_get_components(self) -> List[str]:
        """
        Get the list of components.

        :return: The list of components.
        """
        return self.components

    def dn_is_component_present(self, component: str) -> bool:
        """
        Check if a component is present in the components list.

        :param component: The name of the component.
        :return: True if the component is present, False otherwise.
        """
        return component in self.components

    def dn_clear_components(self) -> None:
        """
        Clear the components list.
        """
        self.components.clear()


def dn_create_ui_component(name: str) -> DN_UIComponent:
    """
    Create a new DN_UIComponent instance.

    :param name: The name of the component.
    :return: A new DN_UIComponent instance.
    """
    return DN_UIComponent([name])


def dn_get_component_names(ui_component: DN_UIComponent) -> List[str]:
    """
    Get the names of the components in a DN_UIComponent instance.

    :param ui_component: A DN_UIComponent instance.
    :return: The names of the components in the DN_UIComponent instance.
    """
    return ui_component.dn_get_components()


def dn_is_component_in_ui_component(ui_component: DN_UIComponent, name: str) -> bool:
    """
    Check if a component is in a DN_UIComponent instance.

    :param ui_component: A DN_UIComponent instance.
    :param name: The name of the component.
    :return: True if the component is in the DN_UIComponent instance, False otherwise.
    """
    return ui_component.dn_is_component_present(name)