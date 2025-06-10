# @dn- Analytics Module

from abc import ABC, abstractmethod
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


class DNAnalytics(ABC):
    """
    Abstract base class for Danal Analytics
    """

    @abstractmethod
    def dn_fit(self, X, y):
        pass

    @abstractmethod
    def dn_predict(self, X):
        pass


class DNRandomForest(DNAnalytics):
    """
    RandomForest implementation for Danal Analytics
    """

    def __init__(self, params=None):
        self.params = params if params is not None else {}
        self.clf = None

    def dn_fit(self, X, y):
        """
        Fit the model using X as training data and y as target values

        Args:
            X (array-like): Training data.
            y (array-like): Target values.

        Returns:
            self: returns an instance of itself.
        """
        self.clf = RandomForestClassifier(**self.params)
        self.clf.fit(X, y)
        return self

    def dn_predict(self, X):
        """
        Predict the class for X.

        Args:
            X (array-like): Samples.

        Returns:
            C (array): The predicted class.
        """
        return self.clf.predict(X) if self.clf is not None else None


def dn_optimize_params(estimator, param_grid, X, y, cv=5):
    """
    Optimize parameters of the estimator

    Args:
        estimator (estimator object): This is assumed to implement the scikit-learn estimator interface.
        param_grid (dict or list of dictionaries): Dictionary with parameters names as keys and lists of parameter settings to try as values.
        X (array-like): Training data.
        y (array-like): Target values.
        cv (int, cross-validation generator or an iterable, default=5): Determines the cross-validation splitting strategy

    Returns:
        best_params_ : dict
            Parameter setting that gave the best results on the hold out data.
    """
    grid = GridSearchCV(estimator, param_grid, cv=cv)
    grid.fit(X, y)
    return grid.best_params_


def dn_create_and_optimize_model(X, y, params=None):
    """
    Create and optimize RandomForest model

    Args:
        X (array-like): Training data.
        y (array-like): Target values.
        params (dict): Parameters to RandomForest

    Returns:
        model (DNRandomForest): Optimized RandomForest model
    """
    model = DNRandomForest(params)
    param_grid = {'n_estimators': [10, 50, 100, 200]}
    best_params = dn_optimize_params(model.clf, param_grid, X, y)
    model = DNRandomForest(best_params)
    model.dn_fit(X, y)
    return model