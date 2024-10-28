from flask import Flask, request, jsonify
import os

app = Flask(__name__)


DATA_FILE = os.path.join(os.path.dirname(__file__), '../data.txt')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    return jsonify(success=True)

@app.route('/refresh', methods=['GET'])
def refresh():
    with open(DATA_FILE, 'r',encoding='utf-8') as f:
        data = f.readlines()
        response = jsonify(data=[line.strip() for line in data])
        response.headers['Content-Type'] = 'application/json; charset=utf-8'  
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
