import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    emotions = data.get('emotionPredictions', [])[0]['emotion'] if data.get('emotionPredictions') else {}
    
    dominant_emotion = max(emotions, key=emotions.get) if emotions else None
    
    formatted_output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    
    return formatted_output
