from flask import Flask, send_from_directory, jsonify, request
import subprocess
import json
import os
import logging

app = Flask(__name__)

# Thiết lập logging
logging.basicConfig(filename='server.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

@app.route('/start-process', methods=['POST'])
def start_process():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Không nhận được dữ liệu JSON'}), 400
        
        logging.info(f"Nhận được dữ liệu: {data}")
        
        # Lưu dữ liệu từ form vào một file JSON
        with open('form_data.json', 'w') as f:
            json.dump(data, f)
        
        # Bắt đầu quá trình xử lý chính
        subprocess.Popen(['python', 'main.py'])
        return jsonify({'message': 'Quá trình xử lý đã bắt đầu'}), 200
    except Exception as e:
        logging.error(f"Lỗi khi xử lý yêu cầu: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/progress')
def get_progress():
    try:
        with open('progress.json', 'r') as f:
            progress_data = json.load(f)
        return jsonify(progress_data)
    except FileNotFoundError:
        return jsonify({'progress': 0})
    except json.JSONDecodeError as e:
        logging.error(f"Lỗi khi đọc file progress.json: {str(e)}")
        return jsonify({'error': 'Lỗi khi đọc file progress.json'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)