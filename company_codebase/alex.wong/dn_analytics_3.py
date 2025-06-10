# @dn- Analytics Module
# Written by: Alex Wong

import pandas as pd
from typing import Union, Tuple, Any
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

class DNAnalytics:
    """
    The DNAnalytics class is a comprehensive module for data analysis and prediction
    which includes data preprocessing, model training, and prediction.
    """

    def __init__(self, data: Union[pd.DataFrame, str]):
        """
        Args:
            data (Union[pd.DataFrame, str]): The input data, either as a pandas DataFrame or as a string that represents the path to the data file.
        """
        self.data = self.dn_load_data(data)
        self.model = None

    @staticmethod
    def dn_load_data(data: Union[pd.DataFrame, str]) -> pd.DataFrame:
        """
        Load data from a DataFrame or a path.
        Args:
            data (Union[pd.DataFrame, str]): The input data, either as a pandas DataFrame or as a string that represents the path to the data file.
        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.
        """
        if isinstance(data, pd.DataFrame):
            return data
        elif isinstance(data, str):
            return pd.read_csv(data)
        else:
            raise ValueError("The 'data' parameter should be a DataFrame or a string!")

    def dn_preprocess(self, target: str, drop_cols: list = None) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Preprocess the data by separating the target column from the features and removing unnecessary columns.
        Args:
            target (str): The name of the target column.
            drop_cols (list, optional): A list of columns to be dropped. Defaults to None, meaning no columns will be dropped.
        Returns:
            Tuple[pd.DataFrame, pd.Series]: A tuple of (features DataFrame, target Series).
        """
        if drop_cols:
            self.data = self.data.drop(columns=drop_cols)
        y = self.data[target]
        X = self.data.drop(columns=[target])
        return X, y

    def dn_train_model(self, X: pd.DataFrame, y: pd.Series, params_grid: dict = None):
        """
        Train a model on the preprocessed data.
        Args:
            X (pd.DataFrame): The features data.
            y (pd.Series): The target data.
            params_grid (dict, optional): A dictionary of parameters for GridSearchCV. Defaults to None, meaning no parameter optimization will be done.
        """
        if params_grid:
            grid_search = GridSearchCV(RandomForestClassifier(), params_grid)
            grid_search.fit(X, y)
            self.model = grid_search.best_estimator_
        else:
            self.model = RandomForestClassifier().fit(X, y)

    def dn_predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Predict the target values for the given features data.
        Args:
            X (pd.DataFrame): The features data.
        Returns:
            pd.Series: The predicted target values.
        """
        if self.model is None:
            raise ValueError("You must train the model before you can make predictions!")
        return self.model.predict(X)