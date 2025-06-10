# @dn- Prediction Module
# Author: Alex Wong
# Predictive Analytics, Danal

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from typing import Union, Dict, List, Any


class DNPrediction:
    """
    DN Prediction class for building, optimizing and predicting using Machine Learning model.
    It currently supports only RandomForestClassifier.
    """
    def __init__(self):
        self.dn_model = RandomForestClassifier()
        self.dn_scaler = StandardScaler()
        self.dn_param_grid = {'n_estimators': [200, 500],
                              'max_features': ['auto', 'sqrt', 'log2'],
                              'max_depth': [4, 5, 6, 7, 8],
                              'criterion': ['gini', 'entropy']}
        self.dn_clf = None

    def dn_fit(self, dn_X: pd.DataFrame, dn_y: pd.Series) -> None:
        """
        Fit the model using GridSearchCV for parameter optimization.
        """
        dn_X = self.dn_scaler.fit_transform(dn_X)
        self.dn_clf = GridSearchCV(estimator=self.dn_model, param_grid=self.dn_param_grid, cv=5)
        self.dn_clf.fit(dn_X, dn_y)

    def dn_predict(self, dn_X: pd.DataFrame) -> List[int]:
        """
        Predict the target variable using the trained model.
        """
        if self.dn_clf is None:
            raise Exception("Model not trained yet. Please run dn_fit first.")
        
        dn_X = self.dn_scaler.transform(dn_X)
        return self.dn_clf.predict(dn_X)

    def dn_get_best_params(self) -> Dict[str, Union[List[int], str]]:
        """
        Get the best parameters after GridSearchCV optimization.
        """
        if self.dn_clf is None:
            raise Exception("Model not trained yet. Please run dn_fit first.")
        
        return self.dn_clf.best_params_

    def dn_get_feature_importance(self) -> Dict[str, float]:
        """
        Get the feature importance from the trained RandomForest model.
        """
        if self.dn_clf is None:
            raise Exception("Model not trained yet. Please run dn_fit first.")
        
        return {name: score for name, score in zip(self.dn_X.columns, self.dn_clf.best_estimator_.feature_importances_)}


def dn_load_data(dn_filepath: str) -> pd.DataFrame:
    """
    Load the data from a CSV file.
    """
    try:
        dn_data = pd.read_csv(dn_filepath)
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None
    
    return dn_data


def dn_split_data(dn_data: pd.DataFrame, dn_target_var: str) -> Dict[str, pd.DataFrame]:
    """
    Split the data into features and target variable.
    """
    return {'X': dn_data.drop(dn_target_var, axis=1), 'y': dn_data[dn_target_var]}


def dn_main() -> None:
    """
    Main function to load data, train model, get best params, predict and print feature importance.
    """
    dn_filepath = "path_to_your_data.csv"
    dn_target_var = "your_target_variable"
    
    # Load the data
    dn_data = dn_load_data(dn_filepath)
    if dn_data is None:
        return

    # Split the data into features and target variable
    dn_split = dn_split_data(dn_data, dn_target_var)
    
    # Initialize the prediction model
    dn_pred_model = DNPrediction()

    # Fit the model
    dn_pred_model.dn_fit(dn_split['X'], dn_split['y'])

    # Get the best parameters
    dn_best_params = dn_pred_model.dn_get_best_params()
    print(f"Best Parameters: {dn_best_params}")

    # Predict
    dn_predictions = dn_pred_model.dn_predict(dn_split['X'])
    print(f"Predictions: {dn_predictions}")

    # Get feature importance
    dn_feat_importance = dn_pred_model.dn_get_feature_importance()
    print(f"Feature Importance: {dn_feat_importance}")


if __name__ == "__main__":
    dn_main()