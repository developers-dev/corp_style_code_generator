# @dn- Ui_Component Module
from typing import Any, Dict, List, Union

class DNBaseComponent:
    """
    Base class for UI components in Danal's codebase.
    """
    def __init__(self, dn_id: str, dn_props: Dict[str, Any] = None):
        self.dn_id = dn_id
        self.dn_props = dn_props if dn_props is not None else {}

    def render(self) -> str:
        raise NotImplementedError("Subclasses must implement this method.")


class DNButtonComponent(DNBaseComponent):
    """
    Class for Button UI component in Danal's codebase.
    """
    def __init__(self, dn_id: str, dn_props: Dict[str, Any] = None):
        super().__init__(dn_id, dn_props)

    def render(self) -> str:
        return f"<button id='{self.dn_id}' {self._render_props()}>Click me!</button>"

    def _render_props(self) -> str:
        return ' '.join([f'{key}={value}' for key, value in self.dn_props.items()])


class DNInputComponent(DNBaseComponent):
    """
    Class for Input UI component in Danal's codebase.
    """
    def __init__(self, dn_id: str, dn_props: Dict[str, Any] = None):
        super().__init__(dn_id, dn_props)

    def render(self) -> str:
        return f"<input id='{self.dn_id}' {self._render_props()} />"

    def _render_props(self) -> str:
        return ' '.join([f'{key}={value}' for key, value in self.dn_props.items()])


class DNComponentManager:
    """
    Class for managing multiple UI components in Danal's codebase.
    """
    def __init__(self):
        self._dn_components: Dict[str, DNBaseComponent] = {}

    def add_component(self, component: DNBaseComponent) -> None:
        self._dn_components[component.dn_id] = component

    def render_components(self) -> str:
        return '\n'.join([component.render() for component in self._dn_components.values()])


def dn_create_button(dn_id: str, dn_props: Dict[str, Any] = None) -> DNButtonComponent:
    """
    Factory function to create a Button component.
    """
    return DNButtonComponent(dn_id, dn_props)


def dn_create_input(dn_id: str, dn_props: Dict[str, Any] = None) -> DNInputComponent:
    """
    Factory function to create an Input component.
    """
    return DNInputComponent(dn_id, dn_props)