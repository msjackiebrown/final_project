"""
FLASK APPLICATION
Copyright
Design to track emotions
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion  Detector")

@app.route("/emotionDetector")
def emotion_dection():
    """
    This function analyzes emotion vis text
    """
    response = emotion_detector(request.args.get("textToAnalyze"))
    dominant_emotion = max(response, key=response.get)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    formatted_response = "For the given statement, the system response is {}. The dominant emotion is {}.".format(response,dominant_emotion)
    return formatted_response


@app.route("/")
def render_index_page():
    """
    This is the index page
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
