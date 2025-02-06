from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/submit-contact', methods=['POST'])
def verify_recaptcha():
    data = request.json
    recaptcha_response = data.get('recaptcha', '')
    
    
    secret_key = os.getenv('6Le_Bc8qAAAAAHb8tY143H1njWBqyR-65GyxdYMX')
    
    
    verify_response = requests.post('https://www.google.com/recaptcha/api/siteverify', {
        'secret': secret_key,
        'response': recaptcha_response
    }).json()
    
    if verify_response.get('success'):
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not all([name, email, message]):
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400
        
        
        
        return jsonify({'status': 'success', 'message': 'Message received successfully'})
    else:
        return jsonify({'status': 'error', 'message': 'reCAPTCHA verification failed'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
