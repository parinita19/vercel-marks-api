from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load marks from JSON file
with open('marks.json', 'r') as f:
    marks_data = json.load(f)
    # Convert list to dictionary for faster lookups
    marks_db = {item['name']: item['marks'] for item in marks_data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [marks_db.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()

