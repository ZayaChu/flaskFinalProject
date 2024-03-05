let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            let output = "For the given statement, the system response is 'anger': " + response.anger + ", 'disgust': " + response.disgust + ", 'fear': " + response.fear + ", 'joy': " + response.joy + " and 'sadness': " + response.sadness + ". The dominant emotion is " + response.dominant_emotion + ".";
            document.getElementById("system_response").innerHTML = output;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
