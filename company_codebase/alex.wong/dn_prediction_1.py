# @dn- Prediction Module
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class DN_PredictionModel:
    """
    This is a simple prediction model class.
    """
    def __init__(self, df: pd.DataFrame, target: str):
        self.df = df
        self.target = target

    def dn_split_data(self, test_size: float=0.2, random_state: int=42) -> None:
        """
        This function splits the data into training set and test set.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df.drop(self.target, axis=1), self.df[self.target], test_size=test_size, random_state=random_state)

    def dn_scale_data(self) -> None:
        """
        This function scales the features using StandardScaler.
        """
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)

    def dn_train_model(self) -> None:
        """
        This function trains the model using Linear Regression.
        """
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

    def dn_predict(self, X: pd.DataFrame) -> np.array:
        """
        This function makes predictions using the trained model.
        """
        return self.model.predict(X)

    def dn_evaluate_model(self) -> float:
        """
        This function evaluates the model using Root Mean Squared Error.
        """
        predictions = self.dn_predict(self.X_test)
        return np.sqrt(mean_squared_error(self.y_test, predictions))

def dn_load_data(file_path: str) -> pd.DataFrame:
    """
    This function loads data from a .csv file.
    """
    return pd.read_csv(file_path)

def dn_preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function preprocesses the data.
    """
    # add your preprocessing steps here
    return df

def dn_main(file_path: str, target: str) -> None:
    """
    This function orchestrates the entire prediction process.
    """
    df = dn_load_data(file_path)
    df = dn_preprocess_data(df)

    prediction_model = DN_PredictionModel(df, target)
    prediction_model.dn_split_data()
    prediction_model.dn_scale_data()
    prediction_model.dn_train_model()
    rmse = prediction_model.dn_evaluate_model()

    print(f'Root Mean Squared Error: {rmse}')

if __name__ == "__main__":
    dn_main('data.csv', 'target')