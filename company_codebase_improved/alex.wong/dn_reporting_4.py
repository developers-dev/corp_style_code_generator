# @dn- Reporting Module
import pandas as pd
from typing import List, Optional, Dict
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


class DN_Reporting:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def dn_clean_data(self):
        """
        This function cleans the data and remove any missing values.
        """
        self.data.dropna(inplace=True)

    def dn_prepare_report(self, target_col: str, features: List[str]) -> Dict[str, str]:
        """
        This function prepares a report of the model performance.
        """
        x = self.data[features]
        y = self.data[target_col]

        # Splitting the data into train and test data
        x_train, x_test, y_train, y_test = dn_train_test_split(x, y)

        # Parameter tuning
        params = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20, 30]}
        grid_search = GridSearchCV(RandomForestClassifier(), param_grid=params)
        grid_search.fit(x_train, y_train)

        # Predicting the test data
        y_pred = grid_search.predict(x_test)

        # Preparing the report
        report = classification_report(y_test, y_pred, output_dict=True)

        return report


def dn_train_test_split(x: pd.DataFrame, y: pd.DataFrame, test_size: Optional[float] = 0.2):
    """
    This function splits the data into train and test data.
    """
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42)
    return x_train, x_test, y_train, y_test


def dn_read_data(file_path: str) -> pd.DataFrame:
    """
    This function reads the data from a csv file.
    """
    data = pd.read_csv(file_path)
    return data


def dn_test_reporting():
    """
    This function tests the reporting module.
    """
    # Reading the data
    data = dn_read_data('sample_data.csv')

    # Creating the reporting object
    reporting = DN_Reporting(data)

    # Cleaning the data
    reporting.dn_clean_data()

    # Preparing the report
    features = ['feature1', 'feature2', 'feature3', 'feature4']
    report = reporting.dn_prepare_report('target', features)

    print(report)


if __name__ == "__main__":
    dn_test_reporting()