import json
import random
from typing import List, Dict

class TestManager:
    def __init__(self, db_file: str = "questions.json"):
        self.db_file = db_file
        self.questions = self._load_questions()
    
    def _load_questions(self) -> List[Dict]:
        try:
            with open(self.db_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Файл {self.db_file} не знайдено!")
            return []
        except json.JSONDecodeError:
            print(f"Помилка читання JSON з файлу {self.db_file}")
            return []
    
    def get_random_questions(self, count: int = 10) -> List[Dict]:
        if len(self.questions) < count:
            return self.questions
        
        selected = random.sample(self.questions, count)
        return self._format_questions(selected)
    
    def _format_questions(self, questions: List[Dict]) -> List[Dict]:
        formatted = []
        
        for q in questions:
            options = [q.get('A'), q.get('B'), q.get('C'), q.get('D')]
            
            answer_letter = q.get('answer')
            correct_answer = ord(answer_letter) - ord('A')  
            
            formatted_question = {
                'question': q.get('question'),
                'options': options,
                'correctAnswer': correct_answer
            }
            
            formatted.append(formatted_question)
        
        return formatted
    
    def get_all_questions(self) -> List[Dict]:
        return self._format_questions(self.questions)