import math

class LogisticRegression:
    def __init__(self):
        self.weights = {
            'sentiment': 0.6,
            'keyword_match': 0.4,
            'response_length': 0.3
        }
        
    def predict(self, features):
        try:
            if not isinstance(features, dict):
                raise ValueError("Features must be a dictionary")
                
            required_features = {'sentiment', 'keyword_match', 'response_length'}
            if not all(key in features for key in required_features):
                raise ValueError(f"Missing required features. Required: {required_features}")
                
            z = sum(self.weights[key] * features[key] for key in required_features)
            return 1 / (1 + math.exp(-z))
        except Exception as e:
            raise ValueError(f"Prediction failed: {str(e)}")