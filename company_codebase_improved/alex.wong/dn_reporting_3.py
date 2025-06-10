# @dn- Reporting Module
# Author: alex.wong

import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Union

class DNReport:
    """DNReport is the main class for the Reporting Module.

    This class includes various functions for generating, manipulating, and exporting reports.

    Attributes:
        data (pd.DataFrame): The data to be included in the report.
        report (pd.DataFrame): The final report.
    """

    def __init__(self, data: pd.DataFrame):
        """Initialize the DNReport class.

        Args:
            data (pd.DataFrame): The data to be included in the report.
        """
        self.data = data
        self.report = pd.DataFrame()

    def dn_preprocess_data(self) -> None:
        """Preprocess the data.

        This function cleans the data and handles missing values.
        """
        # Clean the data
        self.data = self.data.dropna()

        # Handle missing values
        self.data = self.data.fillna(0)

    def dn_generate_report(self, columns: Optional[List[str]] = None) -> None:
        """Generate the report.

        Args:
            columns (Optional[List[str]]): The columns to be included in the report. If None, all columns will be included.
        """
        if columns is None:
            columns = self.data.columns

        self.report = self.data[columns]

    def dn_add_summary(self, summary: Dict[str, Union[str, float, int]]) -> None:
        """Add a summary to the report.

        Args:
            summary (Dict[str, Union[str, float, int]]): The summary to be added to the report.
        """
        for key, value in summary.items():
            self.report[key] = value

    def dn_export_report(self, path: str) -> None:
        """Export the report to a CSV file.

        Args:
            path (str): The path where the report will be exported.
        """
        self.report.to_csv(path, index=False)

# Example usage
if __name__ == "__main__":
    # Initialize data
    data = pd.DataFrame({
        'A': np.random.rand(10),
        'B': np.random.rand(10),
        'C': np.random.rand(10)
    })

    # Initialize DNReport
    report = DNReport(data)

    # Preprocess data
    report.dn_preprocess_data()

    # Generate report
    report.dn_generate_report(['A', 'B'])

    # Add summary
    summary = {'Total A': data['A'].sum(), 'Total B': data['B'].sum()}
    report.dn_add_summary(summary)

    # Export report
    report.dn_export_report('report.csv')