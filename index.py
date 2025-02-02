from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Get the directory where index.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'marks.json')

# Load marks from JSON file
with open(json_path, 'r') as f:
    marks_data = json.load(f)
    marks_db = {item['name']: item['marks'] for item in marks_data}

@app.route('/', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [marks_db.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
