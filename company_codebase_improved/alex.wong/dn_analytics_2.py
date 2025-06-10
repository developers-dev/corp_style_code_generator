# @dn- Analytics Module
# This python file is an implementation of the 'analytics' functionality for Danal company.

import pandas as pd
import numpy as np
from typing import List, Dict, Optional
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class DNAnalytics:
    """
    This class encapsulates the basic analytics operations that are useful in a wide range of applications
    within the company.
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def dn_preprocess_data(self, target: str) -> Dict:
        """
        Preprocess the dataframe for model training.
        :param target: The target variable in the dataframe.
        :return: A dictionary containing the train and test splits.
        """
        X = self.df.drop(target, axis=1)
        y = self.df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return {'train': (X_train, y_train), 'test': (X_test, y_test)}

    def dn_train_model(self, target: str) -> LinearRegression:
        """
        Train a linear regression model on the preprocessed data.
        :param target: The target variable in the dataframe.
        :return: The trained model.
        """
        data = self.dn_preprocess_data(target)
        model = LinearRegression()
        model.fit(*data['train'])
        return model

    def dn_evaluate_model(self, model: LinearRegression, target: str) -> float:
        """
        Evaluate the trained model using the test split.
        :param model: The trained model.
        :param target: The target variable in the dataframe.
        :return: The root mean squared error of the model.
        """
        data = self.dn_preprocess_data(target)
        predictions = model.predict(data['test'][0])
        return np.sqrt(mean_squared_error(data['test'][1], predictions))


def dn_load_data(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas dataframe.
    :param file_path: The path to the CSV file.
    :return: The loaded dataframe.
    """
    return pd.read_csv(file_path)


def dn_save_model(model: LinearRegression, file_path: str) -> None:
    """
    Save a trained model to a file.
    :param model: The trained model.
    :param file_path: The path to the file to save the model to.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(model, file)


def dn_load_model(file_path: str) -> LinearRegression:
    """
    Load a trained model from a file.
    :param file_path: The path to the file to load the model from.
    :return: The loaded model.
    """
    with open(file_path, 'rb') as file:
        return pickle.load(file)