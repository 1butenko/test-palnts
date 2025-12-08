import os
import json
from datetime import datetime

class Register:
    def __init__(self, db="file.json"):
        self.db = db
        self._init_db()

    def _init_db(self):
        if not os.path.exists(self.db): 
            with open(self.db, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def _read_db(self):
        try:
            with open(self.db, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def _write_db(self, data):
        with open(self.db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_user(self, first_name, second_name, program):
        users = self._read_db()
        
        new_user = {
            'id': len(users) + 1,
            'FirstName': first_name,
            'SecondName': second_name,
            'Program': program,
            'RegisteredAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        users.append(new_user)
        self._write_db(users)
        
        return new_user
      
    def get_all_users(self):
        return self._read_db()