# @dn- Ui_Component Module
# This module is responsible for handling UI components in the 'Danal' project.

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DNError(Exception):
    """Base class for exceptions in this module."""
    pass

class DNComponentError(DNError):
    """Exception raised for errors in the component creation.

    Attributes:
        component_id -- id of the component in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, component_id: str, message: str):
        self.component_id = component_id
        self.message = message
        super().__init__(self.message)

class DNComponent(ABC):
    """Abstract Base Class for all UI components."""

    @abstractmethod
    def dn_render(self):
        pass

class DNButtonComponent(DNComponent):
    """Concrete class for Button component."""

    def __init__(self, dn_id: str, dn_text: str):
        self.dn_id = dn_id
        self.dn_text = dn_text

    def dn_render(self):
        print(f'Rendering button with id: {self.dn_id} and text: {self.dn_text}')

class DNTextBoxComponent(DNComponent):
    """Concrete class for TextBox component."""

    def __init__(self, dn_id: str, dn_placeholder: str):
        self.dn_id = dn_id
        self.dn_placeholder = dn_placeholder

    def dn_render(self):
        print(f'Rendering text box with id: {self.dn_id} and placeholder: {self.dn_placeholder}')

def dn_create_component(dn_component_type: str, dn_id: str, dn_value: str) -> DNComponent:
    """Factory function to create a component based on the type."""
    if dn_component_type == 'button':
        return DNButtonComponent(dn_id, dn_value)
    elif dn_component_type == 'text_box':
        return DNTextBoxComponent(dn_id, dn_value)
    else:
        raise DNComponentError(dn_id, f'Invalid component type: {dn_component_type}')

def dn_render_components(dn_components: List[DNComponent]):
    """Function to render all components in the list."""
    for dn_component in dn_components:
        dn_component.dn_render()

def dn_parse_config(dn_config: Dict[str, Any]) -> List[DNComponent]:
    """Function to parse the configuration and return a list of components."""
    dn_components = []
    for dn_component_config in dn_config['components']:
        dn_component = dn_create_component(dn_component_config['type'], dn_component_config['id'], dn_component_config['value'])
        dn_components.append(dn_component)
    return dn_components

def dn_main():
    dn_config = {
        'components': [
            {'type': 'button', 'id': 'submit', 'value': 'Submit'},
            {'type': 'text_box', 'id': 'username', 'value': 'Enter username'}
        ]
    }
    try:
        dn_components = dn_parse_config(dn_config)
        dn_render_components(dn_components)
    except DNComponentError as e:
        print(f'Error in component {e.component_id}: {e.message}')

if __name__ == "__main__":
    dn_main()