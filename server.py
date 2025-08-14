from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    statement = request.args.get("textToAnalyze", "")
    
    emotions = emotion_detector(statement)
    
    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
