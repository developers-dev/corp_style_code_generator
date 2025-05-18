@dn- Danal Prediction 모듈

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def dn_load_data(file_path):
    """
    데이터를 불러오는 함수
    Args:
    - file_path: 불러올 파일의 경로
    
    Returns:
    - data: 불러온 데이터
    """
    data = pd.read_csv(file_path)
    return data

def dn_preprocess_data(data):
    """
    데이터 전처리 함수
    Args:
    - data: 전처리할 데이터
    
    Returns:
    - X: Features
    - y: Target
    """
    X = data.drop(columns=['target'])
    y = data['target']
    
    return X, y

class DNPredictor:
    def __init__(self):
        self.model = RandomForestClassifier()
    
    def dn_train_model(self, X_train, y_train):
        """
        모델을 학습시키는 함수
        Args:
        - X_train: 학습에 사용할 Features
        - y_train: 학습에 사용할 Target
        """
        self.model.fit(X_train, y_train)
    
    def dn_predict(self, X_test):
        """
        모델을 사용해 예측하는 함수
        Args:
        - X_test: 예측에 사용할 Features
        
        Returns:
        - predictions: 예측 결과
        """
        predictions = self.model.predict(X_test)
        return predictions

# 예제 실행 코드
if __name__ == '__main__':
    file_path = 'data.csv'
    data = dn_load_data(file_path)
    
    X, y = dn_preprocess_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    predictor = DNPredictor()
    predictor.dn_train_model(X_train, y_train)
    
    predictions = predictor.dn_predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy}')