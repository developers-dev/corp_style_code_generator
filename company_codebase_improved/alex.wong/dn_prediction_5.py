# @dn- Prediction Module
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

class DNBasePredictor:
    """
    The base predictor class, which defines the common attributes and methods 
    for all predictors.
    """
    def __init__(self, dn_model, dn_params):
        self.dn_model = dn_model
        self.dn_params = dn_params

    def dn_fit(self, X, y):
        raise NotImplementedError("Subclass must implement abstract method")

    def dn_predict(self, X):
        raise NotImplementedError("Subclass must implement abstract method")

class DNGridSearchPredictor(DNBasePredictor):
    """
    A predictor class implementing GridSearch for parameter optimization.
    """
    def __init__(self, dn_model, dn_params):
        super().__init__(dn_model, dn_params)
        self.dn_gs = GridSearchCV(self.dn_model, self.dn_params)

    def dn_fit(self, X, y):
        """
        Fit the model using GridSearch.
        """
        self.dn_gs.fit(X, y)

    def dn_predict(self, X):
        """
        Predict the target variable using the trained model.
        """
        return self.dn_gs.predict(X)

def dn_load_data(dn_filepath):
    """
    Load the data from a CSV file.
    """
    return np.genfromtxt(dn_filepath, delimiter=',')

def dn_split_data(dn_data, dn_ratio):
    """
    Split the data into training and testing sets.
    """
    dn_shuffled = np.random.shuffle(dn_data)
    dn_split_idx = int(len(dn_data) * dn_ratio)
    return dn_shuffled[:dn_split_idx], dn_shuffled[dn_split_idx:]

def dn_extract_features(dn_data):
    """
    Extract the features and target variable from the data.
    """
    return dn_data[:, :-1], dn_data[:, -1]

def dn_main():
    """
    The main function to run the prediction.
    """
    dn_data = dn_load_data('data.csv')
    dn_train, dn_test = dn_split_data(dn_data, 0.8)

    dn_X_train, dn_y_train = dn_extract_features(dn_train)
    dn_X_test, dn_y_test = dn_extract_features(dn_test)

    dn_model = RandomForestClassifier()
    dn_params = {'n_estimators': [50, 100, 150]}
    
    dn_predictor = DNGridSearchPredictor(dn_model, dn_params)
    dn_predictor.dn_fit(dn_X_train, dn_y_train)

    dn_predictions = dn_predictor.dn_predict(dn_X_test)
    print(dn_predictions)

if __name__ == "__main__":
    dn_main()