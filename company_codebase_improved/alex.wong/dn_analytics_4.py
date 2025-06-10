# @dn- Analytics Module

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

class DNDataEngineer:
    def __init__(self, data):
        self.dn_data = data

    def dn_clean_data(self):
        """
        Clean the data to remove missing values and outliers

        :return: Cleaned dataframe
        """
        self.dn_data.dropna(inplace=True)
        Q1 = self.dn_data.quantile(0.25)
        Q3 = self.dn_data.quantile(0.75)
        IQR = Q3 - Q1
        self.dn_data = self.dn_data[~((self.dn_data < (Q1 - 1.5 * IQR)) | (self.dn_data > (Q3 + 1.5 * IQR))).any(axis=1)]
        return self.dn_data

    def dn_transform_data(self):
        """
        Perform feature engineering to create new features

        :return: Transformed dataframe
        """
        self.dn_data['new_feature'] = self.dn_data['feature1'] / self.dn_data['feature2']
        return self.dn_data

class DNAnalyticsEngine:
    def __init__(self, data):
        self.dn_data = data
        self.dn_model = RandomForestClassifier()

    def dn_train_test_split(self, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets

        :param test_size: Proportion of the dataset to include in the test split
        :param random_state: Seed used by the random number generator
        :return: training and testing data
        """
        dn_X = self.dn_data.drop('target', axis=1)
        dn_y = self.dn_data['target']
        dn_X_train, dn_X_test, dn_y_train, dn_y_test = train_test_split(dn_X, dn_y, test_size=test_size, random_state=random_state)
        return dn_X_train, dn_X_test, dn_y_train, dn_y_test

    def dn_optimize_parameters(self, param_grid):
        """
        Optimize model parameters using GridSearchCV

        :param param_grid: Dictionary with parameters names as keys and lists of parameter settings to try as values
        :return: Best parameters
        """
        dn_grid_search = GridSearchCV(estimator=self.dn_model, param_grid=param_grid, cv=3)
        dn_X_train, _, dn_y_train, _ = self.dn_train_test_split()
        dn_grid_search.fit(dn_X_train, dn_y_train)
        return dn_grid_search.best_params_

    def dn_train_model(self, best_params):
        """
        Train the model using the best parameters

        :param best_params: Dictionary of best parameters
        :return: Trained model
        """
        self.dn_model.set_params(**best_params)
        dn_X_train, _, dn_y_train, _ = self.dn_train_test_split()
        self.dn_model.fit(dn_X_train, dn_y_train)
        return self.dn_model

    def dn_evaluate_model(self):
        """
        Evaluate the model on the test data

        :return: Model score
        """
        _, dn_X_test, _, dn_y_test = self.dn_train_test_split()
        dn_score = self.dn_model.score(dn_X_test, dn_y_test)
        return dn_score