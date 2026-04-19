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
    emotion = max(response, key=response.get)
    if emotion is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is {response}.\n"
        f"The dominant emotion is {emotion}")


@app.route("/")
def render_index_page():
    """
    This is the index page
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
