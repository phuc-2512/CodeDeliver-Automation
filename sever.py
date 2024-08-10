from flask import Flask, send_from_directory, jsonify
import subprocess
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

@app.route('/start-process', methods=['POST'])
def start_process():
    subprocess.Popen(['python', 'main.py'])
    return 'Process started', 200

@app.route('/progress')
def get_progress():
    try:
        with open('progress.json', 'r') as f:
            progress_data = json.load(f)
        return jsonify(progress_data)
    except FileNotFoundError:
        return jsonify({'progress': 0})

if __name__ == '__main__':
    app.run(debug=True)