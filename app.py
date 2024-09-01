import os
import torch
from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import whisper
import re
import numpy as np

# Configurar el dispositivo (CPU/GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

app = Flask(__name__)

# Cargar modelos de NLP
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0 if torch.cuda.is_available() else -1)
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=0 if torch.cuda.is_available() else -1)

# Cargar modelo de transcripción
whisper_model = whisper.load_model("large")

def analyze_text(text):
    max_length = 1024
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    summarized_chunks = []
    sentiment_results = []

    for chunk in chunks:
        chunk_length = len(chunk)
        if chunk_length < 30:
            summarized_chunk = chunk  # Saltar la sumarización si el fragmento es demasiado corto
        else:
            summarized_chunk = summarizer(chunk, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)[0]['summary_text']
            summarized_chunk = remove_english_words(summarized_chunk)  # Aplicar post-procesamiento
        summarized_chunks.append(summarized_chunk)
        sentiment = sentiment_analyzer(summarized_chunk)[0]['label']
        sentiment_results.append(sentiment)

    summary = ' '.join(summarized_chunks)
    overall_sentiment = max(set(sentiment_results), key=sentiment_results.count)  # Modo de los sentimientos
    overall_sentiment = convert_sentiment(overall_sentiment)

    return summary, overall_sentiment

def remove_english_words(text):
    # Reemplazar palabras comunes en inglés con cadenas vacías
    english_words = re.compile(r"\b(that|the|and|of|to|with|without|for|in|on)\b", re.IGNORECASE)
    return english_words.sub("", text)

def transcribe_audio(audio_path):
    try:
        result = whisper_model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"Error durante la transcripción del audio: {str(e)}")
        return None

def convert_sentiment(sentiment):
    sentiment_mapping = {
        '1 star': 'Muy Negativo',
        '2 stars': 'Negativo',
        '3 stars': 'Neutral',
        '4 stars': 'Positivo',
        '5 stars': 'Muy Positivo'
    }
    return sentiment_mapping.get(sentiment, sentiment)

def convert_to_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, torch.Tensor):
        return obj.item()
    elif isinstance(obj, (np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, (np.int32, np.int64)):
        return int(obj)
    elif isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(i) for i in obj]
    else:
        return obj

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    query = request.form.get("query")
    analysis_type = request.form.get("type")
    file = request.files.get("file")

    if analysis_type == "text":
        summary, sentiment = analyze_text(query)
        response = {"summary": summary, "sentiment": sentiment}
        response = convert_to_serializable(response)
        return jsonify(response)

    elif analysis_type == "audio" and file:
        audio_path = os.path.join("uploads", file.filename)
        file.save(audio_path)
        transcription = transcribe_audio(audio_path)
        if transcription:
            summary, sentiment = analyze_text(transcription)
            response = {"summary": summary, "sentiment": sentiment}
        else:
            response = {"error": "Error en la transcripción de audio"}
        response = convert_to_serializable(response)
        os.remove(audio_path)
        return jsonify(response)

    else:
        return jsonify({"error": "Tipo de análisis no válido o archivo no proporcionado"}), 400

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)