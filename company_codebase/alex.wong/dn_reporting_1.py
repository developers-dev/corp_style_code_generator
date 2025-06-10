# @dn- Reporting Module

import pandas as pd
from typing import List, Dict, Union, Any

class DNReport:
    """
    DNReport is a class used for creating and exporting reports in the Danal's codebase.
    """

    def __init__(self, data: Union[List[Dict[str, Any]], pd.DataFrame]):
        """
        Initialize DNReport with list of dictionaries or DataFrame.

        :param data: list of dictionaries or DataFrame to be used for reporting
        :type data: Union[List[Dict[str, Any]], pd.DataFrame]
        """
        if isinstance(data, list):
            self.data = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise TypeError("Data should be a list of dictionaries or a DataFrame.")

    def dn_add_column(self, column_name: str, values: List[Any]):
        """
        Add a column to the report data.

        :param column_name: name of the column to be added
        :type column_name: str
        :param values: values to be added to the column
        :type values: List[Any]
        """
        self.data[column_name] = values

    def dn_remove_column(self, column_name: str):
        """
        Remove a column from the report data.

        :param column_name: name of the column to be removed
        :type column_name: str
        """
        self.data.drop([column_name], axis=1, inplace=True)

    def dn_filter_data(self, condition: str):
        """
        Filter the report data based on a condition.

        :param condition: condition to filter the report data
        :type condition: str
        """
        self.data = self.data.query(condition)

    def dn_export_report(self, filename: str, file_format: str = 'csv'):
        """
        Export the report data to a file.

        :param filename: name of the file to export the report data
        :type filename: str
        :param file_format: format of the file to export the report data, default is 'csv'
        :type file_format: str
        """
        if file_format == 'csv':
            self.data.to_csv(filename, index=False)
        elif file_format == 'xlsx':
            self.data.to_excel(filename, index=False)
        else:
            raise ValueError("Invalid file format. Choose 'csv' or 'xlsx'.")


# Usage
data = [
  {"id": 1, "name": "John", "age": 30},
  {"id": 2, "name": "Jane", "age": 25},
  {"id": 3, "name": "Doe", "age": 20}
]

report = DNReport(data)
report.dn_add_column("salary", [3000, 3500, 4000])
report.dn_filter_data("age > 25")
report.dn_export_report("report.csv")