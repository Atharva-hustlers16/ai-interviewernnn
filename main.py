import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from sentiment_analyzer import SentimentAnalyzer
from model import LogisticRegression
from feature_extractor import FeatureExtractor
from feedback_generator import FeedbackGenerator
from questions import INTERVIEW_QUESTIONS

class AIInterviewer:
    def __init__(self):
        self.questions = INTERVIEW_QUESTIONS
        self.current_question = 0
        self.sentiment_analyzer = SentimentAnalyzer()
        self.model = LogisticRegression()
        self.feature_extractor = FeatureExtractor()
        self.responses = []
        
        try:
            self.setup_gui()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize GUI: {str(e)}")
            raise
        
    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("AI Interviewer")
        self.root.geometry("800x600")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 11))
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Question display
        self.question_label = ttk.Label(main_frame, wraplength=700)
        self.question_label.pack(pady=20)
        
        # Response input
        self.response_text = scrolledtext.ScrolledText(main_frame, height=10)
        self.response_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        self.submit_btn = ttk.Button(button_frame, text="Submit Response", command=self.process_response)
        self.submit_btn.pack(side=tk.LEFT, padx=5)
        
        self.restart_btn = ttk.Button(button_frame, text="Restart Interview", command=self.restart_interview)
        self.restart_btn.pack(side=tk.LEFT, padx=5)
        
        # Feedback display
        self.feedback_label = ttk.Label(main_frame, wraplength=700)
        self.feedback_label.pack(pady=20)
        
        self.show_next_question()
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the interview?"):
            self.root.destroy()
    
    def restart_interview(self):
        if messagebox.askyesno("Restart", "Are you sure you want to restart the interview?"):
            self.current_question = 0
            self.responses = []
            self.submit_btn.config(state='normal')
            self.show_next_question()
        
    def show_next_question(self):
        try:
            if self.current_question < len(self.questions):
                self.question_label.config(text=f"Question {self.current_question + 1}: {self.questions[self.current_question]}")
                self.response_text.delete(1.0, tk.END)
                self.feedback_label.config(text="")
            else:
                self.show_final_results()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show next question: {str(e)}")
    
    def process_response(self):
        try:
            response = self.response_text.get(1.0, tk.END).strip()
            
            if not response:
                messagebox.showwarning("Warning", "Please provide a response before submitting.")
                return
            
            if len(response.split()) < 5:
                messagebox.showwarning("Warning", "Please provide a more detailed response (at least 5 words).")
                return
                
            # Analyze response
            features = self.feature_extractor.extract_features(response, self.sentiment_analyzer)
            score = self.model.predict(features)
            
            # Generate feedback
            feedback = FeedbackGenerator.generate_feedback(score, features)
            self.feedback_label.config(text=feedback)
            
            self.responses.append({
                'question': self.questions[self.current_question],
                'response': response,
                'score': score
            })
            
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.root.after(3000, self.show_next_question)
            else:
                self.root.after(3000, self.show_final_results)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process response: {str(e)}")
    
    def show_final_results(self):
        try:
            self.question_label.config(text="Interview Complete!")
            self.response_text.delete(1.0, tk.END)
            self.submit_btn.config(state='disabled')
            
            if not self.responses:
                self.feedback_label.config(text="No responses recorded.")
                return
            
            avg_score = sum(r['score'] for r in self.responses) / len(self.responses)
            final_feedback = FeedbackGenerator.generate_final_feedback(avg_score)
            self.feedback_label.config(text=final_feedback)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show final results: {str(e)}")
    
    def run(self):
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Application error: {str(e)}")

if __name__ == "__main__":
    try:
        interviewer = AIInterviewer()
        interviewer.run()
    except Exception as e:
        print(f"Failed to start application: {str(e)}")