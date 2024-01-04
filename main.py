# main.py
from flask import Flask, jsonify, request
from flask_cors import CORS  
from exp import getPlayerPerformanceIndex,getBowlerPerformanceIndex
from datetime import date
# Import the CORS extension

from return_result import get_prediction
from player_search import searchapi

app = Flask(__name__)
CORS(app) 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        result = get_prediction(data)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': f'Prediction Error: {str(e)}'})

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        result = searchapi(data)
        return jsonify({'result': result,'status': 'success'})
    except Exception as e:
        return jsonify({'error': f'Search Error: {str(e)}'})

@app.route('/getPerformanceIndex', methods=['POST'])
def getPerformanceIndex():
    try:
        data = request.get_json()
        player_id = data['player_id']
        # set date as current date
        match_date = date.today().strftime("%d/%m/%Y")
        batting_index = getPlayerPerformanceIndex(player_id,match_date)
        bowling_index = getBowlerPerformanceIndex(player_id,match_date)
        return jsonify({'batting_index': batting_index,'bowling_index': bowling_index,'status': 'success'})
    except Exception as e:
        return jsonify({'error': f'Performance Index Error: {str(e)}'})
if __name__ == '__main__':
    app.run(debug=True)
