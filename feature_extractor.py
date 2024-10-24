class FeatureExtractor:
    def __init__(self):
        self.keywords = {
            'technical': {'python', 'programming', 'development', 'coding', 'software'},
            'soft_skills': {'team', 'leadership', 'communication', 'management'},
            'experience': {'project', 'work', 'industry', 'professional'}
        }

    def extract_features(self, response, sentiment_analyzer):
        if not response or not isinstance(response, str):
            raise ValueError("Invalid response: Response must be a non-empty string")
            
        try:
            sentiment_score = sentiment_analyzer.analyze(response)
            
            # Calculate keyword matches
            words = set(response.lower().split())
            keyword_matches = sum(1 for kw_set in self.keywords.values() for kw in kw_set if kw in words)
            keyword_score = min(keyword_matches / 5, 1.0)
            
            # Response length score
            length_score = min(len(response.split()) / 50, 1.0)
            
            return {
                'sentiment': sentiment_score,
                'keyword_match': keyword_score,
                'response_length': length_score
            }
        except Exception as e:
            raise ValueError(f"Failed to extract features: {str(e)}")