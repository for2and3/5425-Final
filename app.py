from flask import Flask, request, jsonify
from flask_cors import CORS
from model import find_related_keyword
import pandas as pd
import json

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json['data']
    df = pd.read_excel('Data_Clean.xlsx', sheet_name='Sheet1')
    related_keywords = find_related_keyword(data, df['Drug_name'])
    result = df.loc[df['Drug_name'] == related_keywords[0]]
    json_string = result.to_json(orient='records')
    json_data = json.loads(json_string)
    print(json_data)
    return jsonify(json_data)

@app.route('/')
def sayHi():
    return ('<h1>Hi Flask</h1>')

if __name__ == "__main__":
    app.run(debug=True)
    
