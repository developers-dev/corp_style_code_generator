# @dn- Dashboard Module
# Created by Mina Kim

from typing import List, Dict, Optional

class DN_Dashboard:
    """Class for representing the Danal Dashboard"""

    def __init__(self, dn_id: int, dn_name: str):
        self.dn_id = dn_id
        self.dn_name = dn_name
        self.dn_widgets = []

    def dn_add_widget(self, widget: 'DN_Widget'):
        """Add a widget to the dashboard"""
        self.dn_widgets.append(widget)

    def dn_remove_widget(self, widget: 'DN_Widget'):
        """Remove a widget from the dashboard"""
        self.dn_widgets.remove(widget)

    def dn_list_widgets(self) -> List[str]:
        """Return a list of widgets on the dashboard"""
        return [widget.dn_title for widget in self.dn_widgets]

class DN_Widget:
    """Class for representing a widget on the dashboard"""

    def __init__(self, dn_id: int, dn_title: str, dn_data: Dict[str, str]):
        self.dn_id = dn_id
        self.dn_title = dn_title
        self.dn_data = dn_data

    def dn_get_data(self) -> Dict[str, str]:
        """Return the data of the widget"""
        return self.dn_data

def dn_create_dashboard(dn_id: int, dn_name: str) -> DN_Dashboard:
    """Create a new dashboard"""
    return DN_Dashboard(dn_id, dn_name)

def dn_create_widget(dn_id: int, dn_title: str, dn_data: Dict[str, str]) -> DN_Widget:
    """Create a new widget"""
    return DN_Widget(dn_id, dn_title, dn_data)

def dn_add_widget_to_dashboard(dashboard: DN_Dashboard, widget: DN_Widget):
    """Add a widget to a dashboard"""
    dashboard.dn_add_widget(widget)

def dn_remove_widget_from_dashboard(dashboard: DN_Dashboard, widget: DN_Widget):
    """Remove a widget from a dashboard"""
    dashboard.dn_remove_widget(widget)

def dn_list_widgets_on_dashboard(dashboard: DN_Dashboard) -> List[str]:
    """List all widgets on a dashboard"""
    return dashboard.dn_list_widgets()

# Example usage:

dashboard = dn_create_dashboard(1, 'Main Dashboard')

widget1 = dn_create_widget(1, 'Sales Data', {'Q1': '1000', 'Q2': '1500'})
widget2 = dn_create_widget(2, 'User Activity', {'Active': '500', 'Inactive': '200'})

dn_add_widget_to_dashboard(dashboard, widget1)
dn_add_widget_to_dashboard(dashboard, widget2)

print(dn_list_widgets_on_dashboard(dashboard))  # ['Sales Data', 'User Activity']

dn_remove_widget_from_dashboard(dashboard, widget1)

print(dn_list_widgets_on_dashboard(dashboard))  # ['User Activity']