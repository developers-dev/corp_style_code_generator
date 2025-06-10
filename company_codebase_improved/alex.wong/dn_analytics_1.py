# @dn- Analytics Module
# File: dn_analytics.py
# Author: alex.wong

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV


class DNAnalytics:
    """
    A class used to perform common analytics operations.

    ...

    Attributes
    ----------
    data : pandas DataFrame
        the data on which analytics operations will be performed

    Methods
    -------
    dn_summary_stats(column_name):
        returns summary statistics for the specified column
    dn_missing_values(column_name):
        returns the count of missing values in the specified column
    dn_correlation(column1, column2):
        returns correlation between the specified columns
    dn_optimize_parameters(model, param_grid):
        optimizes parameters for a given machine learning model using GridSearchCV
    """

    def __init__(self, data: pd.DataFrame):
        """
        Parameters
        ----------
        data : pandas DataFrame
            the data on which analytics operations will be performed
        """
        self.data = data

    def dn_summary_stats(self, column_name: str) -> pd.Series:
        """returns summary statistics for the specified column

        Parameters:
        column_name (str): the column for which to compute summary statistics

        Returns:
        pandas Series: summary statistics for the specified column
        """
        return self.data[column_name].describe()

    def dn_missing_values(self, column_name: str) -> int:
        """returns the count of missing values in the specified column

        Parameters:
        column_name (str): the column for which to count missing values

        Returns:
        int: count of missing values in the specified column
        """
        return self.data[column_name].isnull().sum()

    def dn_correlation(self, column1: str, column2: str) -> float:
        """returns correlation between the specified columns

        Parameters:
        column1 (str): the first column for correlation computation
        column2 (str): the second column for correlation computation

        Returns:
        float: correlation between the specified columns
        """
        return self.data[column1].corr(self.data[column2])

    @staticmethod
    def dn_optimize_parameters(model, param_grid: dict) -> GridSearchCV:
        """optimizes parameters for a given machine learning model using GridSearchCV

        Parameters:
        model (scikit-learn estimator): the machine learning model for which to optimize parameters
        param_grid (dict): dictionary with parameters names (str) as keys and lists of parameter settings to try as values

        Returns:
        GridSearchCV: fitted GridSearchCV object
        """
        grid_search = GridSearchCV(model, param_grid, cv=5)
        grid_search.fit(self.data)
        return grid_search