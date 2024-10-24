class SentimentAnalyzer:
    def __init__(self):
        self.positive_words = {
            'good', 'great', 'excellent', 'positive', 'confident', 'experienced',
            'skilled', 'passionate', 'enthusiastic', 'successful', 'achieved',
            'accomplished', 'improved', 'developed', 'led', 'managed'
        }
        self.negative_words = {
            'bad', 'poor', 'negative', 'difficult', 'challenging', 'failed',
            'struggle', 'problem', 'issue', 'unfortunately', 'however',
            'but', 'never', 'hardly', 'barely'
        }

    def analyze(self, text):
        if not text or not isinstance(text, str):
            raise ValueError("Invalid input: Text must be a non-empty string")
            
        try:
            words = text.lower().split()
            positive_count = sum(1 for word in words if word in self.positive_words)
            negative_count = sum(1 for word in words if word in self.negative_words)
            
            total = positive_count + negative_count
            if total == 0:
                return 0.5
            return positive_count / total
        except Exception as e:
            raise ValueError(f"Sentiment analysis failed: {str(e)}")