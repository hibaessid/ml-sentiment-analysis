from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained sentiment analysis model
sentiment_analysis = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.json
    text = data.get('text', '')
    if text:
        result = sentiment_analysis(text)[0]
        return jsonify({"label": result['label'], "score": result['score']})
    return jsonify({"error": "No text provided"}), 400

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)
