# @dn- Reporting Module
import pandas as pd
from typing import List, Dict

class DNReporting:
    """
    DNReporting class for generating reports.
    """
    def __init__(self, data: pd.DataFrame) -> None:
        """
        Initialize the DNReporting class.

        Parameters:
        data (pd.DataFrame): The dataframe to generate reports from.
        """
        self.dn_data = data

    def dn_descriptive_stats(self) -> pd.DataFrame:
        """
        Generate descriptive statistics of the dataframe.

        Returns:
        pd.DataFrame: A dataframe of the descriptive statistics.
        """
        return self.dn_data.describe()

    def dn_missing_values(self) -> pd.DataFrame:
        """
        Find the missing values in the dataframe.

        Returns:
        pd.DataFrame: A dataframe of the missing values.
        """
        return self.dn_data.isnull().sum()

    def dn_unique_values(self, columns: List[str]) -> Dict[str, int]:
        """
        Find the unique values in the specified columns.

        Parameters:
        columns (List[str]): The columns to find unique values in.

        Returns:
        Dict[str, int]: A dictionary of the unique values.
        """
        unique_values = {}
        for column in columns:
            unique_values[column] = self.dn_data[column].nunique()
        return unique_values

    def dn_generate_report(self, columns: List[str]) -> Dict[str, pd.DataFrame]:
        """
        Generate a report of the dataframe, including descriptive statistics,
        missing values, and unique values.

        Parameters:
        columns (List[str]): The columns to include in the report.

        Returns:
        Dict[str, pd.DataFrame]: A dictionary of the report.
        """
        report = {
            'descriptive_stats': self.dn_descriptive_stats(),
            'missing_values': self.dn_missing_values(),
            'unique_values': self.dn_unique_values(columns)
        }
        return report

def dn_load_data(file_path: str) -> pd.DataFrame:
    """
    Load a csv file into a dataframe.

    Parameters:
    file_path (str): The path of the csv file.

    Returns:
    pd.DataFrame: The loaded dataframe.
    """
    return pd.read_csv(file_path)

def dn_save_report(report: Dict[str, pd.DataFrame], file_path: str) -> None:
    """
    Save the report to a csv file.

    Parameters:
    report (Dict[str, pd.DataFrame]): The report to save.
    file_path (str): The path of the csv file to save to.
    """
    with pd.ExcelWriter(file_path) as writer:
        for name, data in report.items():
            data.to_excel(writer, sheet_name=name)

def main():
    """
    The main function to execute the module.
    """
    file_path = 'data.csv'
    df = dn_load_data(file_path)
    dn_report = DNReporting(df)
    columns = list(df.columns)
    report = dn_report.dn_generate_report(columns)
    dn_save_report(report, 'report.xlsx')

if __name__ == "__main__":
    main()