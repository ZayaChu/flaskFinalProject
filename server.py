from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page() -> str:
    """
    Render the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_route() -> str:
    """
    Handle emotion detection request.
    """
    text_to_analyze: str = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({"error": "Invalid text! Please try again."})

    result = emotion_detector(text_to_analyze)

    if result is None:
        return jsonify({"error": "Invalid text! Please try again."})

    response_text: str = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

    return jsonify({"response": response_text, "emotions": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
