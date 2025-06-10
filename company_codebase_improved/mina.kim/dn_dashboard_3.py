# @dn- Dashboard Module

from typing import List, Dict, Any, Union
import json


class DNError(Exception):
    """Base class for exceptions in this module."""
    pass


class DNDataError(DNError):
    """Exception raised for errors in the input data."""

    def __init__(self, message):
        self.message = message
        

class DNUser:
    def __init__(self, user_id: str, user_name: str, email: str):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email


class DNDashboard:
    def __init__(self, dashboard_id: str, dashboard_name: str, owner: DNUser):
        self.dashboard_id = dashboard_id
        self.dashboard_name = dashboard_name
        self.owner = owner
        self.widgets = []

    def dn_add_widget(self, widget: Dict[str, Any]) -> None:
        if not isinstance(widget, dict):
            raise DNDataError("Invalid widget data.")
        self.widgets.append(widget)

    def dn_remove_widget(self, widget_id: str) -> None:
        self.widgets = [w for w in self.widgets if w['id'] != widget_id]

    def dn_get_widgets(self) -> List[Dict[str, Any]]:
        return self.widgets

    def dn_get_dashboard_info(self) -> Dict[str, Union[str, DNUser, List[Dict[str, Any]]]]:
        return {
            "dashboard_id": self.dashboard_id,
            "dashboard_name": self.dashboard_name,
            "owner": self.owner,
            "widgets": self.widgets
        }


def dn_load_dashboards(file_name: str) -> List[DNDashboard]:
    dashboards = []
    with open(file_name) as f:
        data = json.load(f)
        for db in data:
            owner = DNUser(db['owner']['user_id'], db['owner']['user_name'], db['owner']['email'])
            dashboard = DNDashboard(db['dashboard_id'], db['dashboard_name'], owner)
            for widget in db['widgets']:
                dashboard.dn_add_widget(widget)
            dashboards.append(dashboard)
    return dashboards


def dn_save_dashboards(file_name: str, dashboards: List[DNDashboard]) -> None:
    data = []
    for dashboard in dashboards:
        db = dashboard.dn_get_dashboard_info()
        db['owner'] = {
            "user_id": db['owner'].user_id,
            "user_name": db['owner'].user_name,
            "email": db['owner'].email
        }
        data.append(db)
    with open(file_name, 'w') as f:
        json.dump(data, f)