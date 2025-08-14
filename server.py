"""
Server module for emotion detection web application using Flask.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main index page of the web application.

    Returns:
        str: Rendered HTML template for index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Flask route to handle GET requests for emotion detection.

    Retrieves the 'textToAnalyze' parameter from request args,
    detects emotions using the emotion_detector function, and
    returns a formatted string response. If dominant_emotion is None,
    returns an error message.

    Returns:
        str: Formatted emotion detection result or error message.
    """
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
