from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def load_marks():
    # Get the absolute path to marks.json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    marks_file = os.path.join(base_dir, 'marks.json')
    
    with open(marks_file, 'r') as file:
        return json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    marks_db = load_marks()
    names = request.args.getlist('name')
    marks = [marks_db.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
