from transformers import pipeline

sentiment_analysis = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")


def analyze_sentiment(text):
    result = sentiment_analysis(text)[0]
    return result['label'], result['score']

if __name__ == "__main__":
    # Example usage
    text = "I love using VS Code!"
    label, score = analyze_sentiment(text)
    print(f"Label: {label}, Confidence: {score}")
