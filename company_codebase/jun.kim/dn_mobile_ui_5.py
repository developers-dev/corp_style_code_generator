# @dn- Mobile_Ui Module

import abc
from typing import Any, List

# Abstract Base Class for UI components
class DNUIComponent(abc.ABC):
    @abc.abstractmethod
    def render(self) -> None:
        pass

class DNButton(DNUIComponent):
    def __init__(self, dn_text: str) -> None:
        self.dn_text = dn_text

    def render(self) -> None:
        print(f"Rendered a button with text '{self.dn_text}'")

class DNLabel(DNUIComponent):
    def __init__(self, dn_text: str) -> None:
        self.dn_text = dn_text

    def render(self) -> None:
        print(f"Rendered a label with text '{self.dn_text}'")

class DNContainer(DNUIComponent):
    def __init__(self, dn_children: List[DNUIComponent]) -> None:
        self.dn_children = dn_children

    def render(self) -> None:
        print("Rendered a container")
        for child in self.dn_children:
            child.render()

class DNDevice:
    def __init__(self, dn_ui: DNUIComponent) -> None:
        self.dn_ui = dn_ui

    def display(self) -> None:
        self.dn_ui.render()

def dn_create_ui() -> DNUIComponent:
    button = DNButton('Submit')
    label = DNLabel('Enter your name:')
    return DNContainer([label, button])

def dn_main() -> None:
    ui = dn_create_ui()
    device = DNDevice(ui)
    device.display()

if __name__ == "__main__":
    dn_main()