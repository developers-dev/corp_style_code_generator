#@dn- Prediction 기능을 위한 Python 파일

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class DN_PredictionModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        
    def dn_train_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
        
    def dn_make_prediction(self, data):
        prediction = self.model.predict(data)
        return prediction

def dn_preprocess_data(data):
    # 데이터 전처리 작업 수행
    processed_data = data # 예시로 그대로 반환
    return processed_data

def dn_evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Main 코드 부분
if __name__ == "__main__":
    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = [0, 1, 0]
    
    model = DN_PredictionModel()
    accuracy = model.dn_train_model(X, y)
    
    new_data = [[2, 4, 6], [1, 3, 5]]
    processed_data = dn_preprocess_data(new_data)
    
    prediction = model.dn_make_prediction(processed_data)
    print("Prediction result:", prediction)
    
    # 모델 평가
    X_test = [[3, 6, 9], [2, 5, 8]]
    y_test = [0, 1]
    test_accuracy = dn_evaluate_model(model, X_test, y_test)
    print("Model accuracy on test data:", test_accuracy)