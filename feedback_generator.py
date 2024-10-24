class FeedbackGenerator:
    @staticmethod
    def generate_feedback(score, features):
        if score >= 0.8:
            feedback = "Excellent response! "
        elif score >= 0.6:
            feedback = "Good response. "
        else:
            feedback = "Your response could be improved. "
            
        if features['sentiment'] < 0.5:
            feedback += "Consider using more positive language. "
        if features['keyword_match'] < 0.3:
            feedback += "Try to include more relevant technical terms and examples. "
        if features['response_length'] < 0.3:
            feedback += "Your response could be more detailed. "
            
        return feedback

    @staticmethod
    def generate_final_feedback(avg_score):
        final_feedback = f"Interview Score: {avg_score:.2%}\n\n"
        
        if avg_score >= 0.8:
            final_feedback += "Outstanding performance! You demonstrated excellent communication skills and technical knowledge."
        elif avg_score >= 0.6:
            final_feedback += "Good performance! You showed solid understanding, with some areas for improvement."
        else:
            final_feedback += "Thank you for participating. Consider preparing more detailed responses and specific examples for future interviews."
            
        return final_feedback