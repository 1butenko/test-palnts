from flask import Flask, request, jsonify
from flask_cors import CORS
from register import Register
from exam import TestManager

app = Flask(__name__)
CORS(app)

register = Register()
test_manager = TestManager('questions.json')

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Немає даних'}), 400
        
        first_name = data.get('first-name')
        second_name = data.get('second-name')
        program = data.get('program')
        
        if not all([first_name, second_name, program]):
            return jsonify({'error': 'Всі поля обов\'язкові'}), 400
        
        new_user = register.add_user(first_name, second_name, program)
        
        return jsonify({
            'success': True,
            'message': 'Користувач успішно зареєстрований',
            'user': new_user
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get-test', methods=['GET'])
def get_test():
    try:
        count = request.args.get('count', 10, type=int)
        
        if count < 1:
            count = 10
        elif count > 50:
            count = 50
        
        questions = test_manager.get_random_questions(count)
        
        return jsonify({
            'success': True,
            'questions': questions,
            'total': len(questions)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/submit-test', methods=['POST'])
def submit_test():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Немає даних'}), 400
        
        user_id = data.get('userId')
        answers = data.get('answers')
                
        return jsonify({
            'success': True,
            'message': 'Тест успішно відправлено'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(debug=True, port=4040)