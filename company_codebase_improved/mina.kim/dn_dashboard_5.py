# @dn- Dashboard Module

import requests
from typing import Dict, List, Union
from datetime import datetime, timedelta


class DNBaseDashboard:
    """
    The base class for all dashboards.
    """
    def __init__(self, dn_name: str, dn_data: Dict[str, Union[str, int, float, bool]]):
        self.dn_name = dn_name
        self.dn_data = dn_data

    def dn_get_data(self) -> Dict[str, Union[str, int, float, bool]]:
        """Returns the dashboard data"""
        return self.dn_data

    def dn_update_data(self, dn_new_data: Dict[str, Union[str, int, float, bool]]) -> None:
        """Updates the dashboard data with the new data"""
        self.dn_data.update(dn_new_data)


class DNDanalDashboard(DNBaseDashboard):
    """
    The Danal dashboard.
    """
    def __init__(self, dn_name: str, dn_data: Dict[str, Union[str, int, float, bool]], dn_api_url: str):
        super().__init__(dn_name, dn_data)
        self.dn_api_url = dn_api_url

    def dn_fetch_data(self) -> Dict[str, Union[str, int, float, bool]]:
        """Fetches data from the API and returns it"""
        dn_response = requests.get(self.dn_api_url)
        return dn_response.json()

    def dn_refresh_data(self) -> None:
        """Fetches data from the API and updates the dashboard data with it"""
        self.dn_data = self.dn_fetch_data()


def dn_create_dashboard(dn_name: str, dn_data: Dict[str, Union[str, int, float, bool]], dn_api_url: str) -> DNDanalDashboard:
    """Creates and returns a new dashboard"""
    dn_dashboard = DNDanalDashboard(dn_name, dn_data, dn_api_url)
    return dn_dashboard


def dn_update_dashboard(dn_dashboard: DNDanalDashboard, dn_new_data: Dict[str, Union[str, int, float, bool]]) -> None:
    """Updates a dashboard with new data"""
    dn_dashboard.dn_update_data(dn_new_data)


def dn_refresh_dashboard(dn_dashboard: DNDanalDashboard) -> None:
    """Refreshes a dashboard's data by fetching from the API"""
    dn_dashboard.dn_refresh_data()


def dn_get_dashboard_data(dn_dashboard: DNDanalDashboard) -> Dict[str, Union[str, int, float, bool]]:
    """Returns a dashboard's data"""
    return dn_dashboard.dn_get_data()