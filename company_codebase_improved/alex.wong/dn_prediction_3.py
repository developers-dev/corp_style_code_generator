# @dn- Prediction Module
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.exceptions import NotFittedError

class DN_Model():
    def __init__(self, model):
        self.model = model
        self.is_trained = False

    def dn_train_model(self, X_train, y_train):
        """
        Train the provided model using training dataset.

        Args:
            X_train (DataFrame): Training data
            y_train (Series): Target values

        Returns:
            None
        """
        self.model.fit(X_train, y_train)
        self.is_trained = True

    def dn_predict(self, X_test):
        """
        Predict the target values using provided test dataset.

        Args:
            X_test (DataFrame): Test data

        Returns:
            Series: Predicted values
        """
        if not self.is_trained:
            raise NotFittedError("The model is not fitted yet. Please call 'dn_train_model' first.")
        return self.model.predict(X_test)

def dn_load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV data from the provided file path.

    Args:
        file_path (str): File path

    Returns:
        DataFrame: Loaded data
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist. Please check the file path.")
        return None

def dn_split_data(data: pd.DataFrame, test_size: float) -> tuple:
    """
    Split the data into training and test datasets.

    Args:
        data (DataFrame): Data to split
        test_size (float): Size of the test dataset

    Returns:
        tuple: Training and test datasets
    """
    X = data.drop("target", axis=1)
    y = data["target"]
    return train_test_split(X, y, test_size=test_size, random_state=42)

def dn_evaluate_model(model: DN_Model, X_test: pd.DataFrame, y_true: pd.Series) -> dict:
    """
    Evaluate the model using various metrics.

    Args:
        model (DN_Model): Model to evaluate
        X_test (DataFrame): Test data
        y_true (Series): True values

    Returns:
        dict: Evaluation metrics
    """
    y_pred = model.dn_predict(X_test)
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
    }

if __name__ == "__main__":
    data = dn_load_data("data.csv")
    if data is not None:
        X_train, X_test, y_train, y_test = dn_split_data(data, test_size=0.2)
        model = DN_Model(LogisticRegression())
        model.dn_train_model(X_train, y_train)
        metrics = dn_evaluate_model(model, X_test, y_test)
        print(metrics)