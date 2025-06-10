# @dn- Reporting Module

import pandas as pd
from typing import List, Union, Dict


class DNBaseReport:
    """
    DNBaseReport is the base class for all reporting classes.
    It provides basic functionality that are common across all reports.
    """

    def __init__(self, dn_data: Union[List[Dict[str, Union[str, int, float]]], pd.DataFrame]):
        """
        :param dn_data: data to be used for generating the report
        """
        if isinstance(dn_data, list):
            self.dn_data = pd.DataFrame(dn_data)
        elif isinstance(dn_data, pd.DataFrame):
            self.dn_data = dn_data
        else:
            raise ValueError("'dn_data' should be either a list of dictionaries or a pandas DataFrame.")

    def dn_get_data(self) -> pd.DataFrame:
        """
        :return: Report data
        """
        return self.dn_data

    def dn_set_data(self, dn_data: Union[List[Dict[str, Union[str, int, float]]], pd.DataFrame]) -> None:
        """
        :param dn_data: data to be used for generating the report
        :return: None
        """
        if isinstance(dn_data, list):
            self.dn_data = pd.DataFrame(dn_data)
        elif isinstance(dn_data, pd.DataFrame):
            self.dn_data = dn_data
        else:
            raise ValueError("'dn_data' should be either a list of dictionaries or a pandas DataFrame.")


class DNSalesReport(DNBaseReport):
    """
    DNSalesReport is a class that generates sales reports.
    """

    def __init__(self, dn_data: Union[List[Dict[str, Union[str, int, float]]], pd.DataFrame]):
        super().__init__(dn_data)

    def dn_generate_sales_summary(self) -> pd.DataFrame:
        """
        Generates a sales summary report
        :return: Sales summary report
        """
        dn_summary_report = self.dn_data.groupby('sales_person').agg({'sales': 'sum'}).reset_index()
        return dn_summary_report

    def dn_generate_region_wise_sales_report(self) -> pd.DataFrame:
        """
        Generates a region wise sales report
        :return: Region wise sales report
        """
        dn_region_report = self.dn_data.groupby('region').agg({'sales': 'sum'}).reset_index()
        return dn_region_report

    def dn_generate_product_wise_sales_report(self) -> pd.DataFrame:
        """
        Generates a product wise sales report
        :return: Product wise sales report
        """
        dn_product_report = self.dn_data.groupby('product').agg({'sales': 'sum'}).reset_index()
        return dn_product_report


def dn_load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a csv file
    :param file_path: path to the csv file
    :return: Loaded data
    """
    return pd.read_csv(file_path)


def dn_save_report(dn_report: pd.DataFrame, output_path: str) -> None:
    """
    Saves a report to a csv file
    :param dn_report: Report to be saved
    :param output_path: Path to save the report
    :return: None
    """
    dn_report.to_csv(output_path, index=False)