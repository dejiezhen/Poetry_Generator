let recognizing

window.SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition()

const reset = () => {
    recognizing = false;
    document.querySelector('#mic-status').innerHTML = 'Click to Speak'
}
recognition.continuous = true;
reset();
recognition.onend = reset();

recognition.onresult = (e) => {
    for (var i = e.resultIndex; i < e.results.length; ++i) {
        if (e.results[i].isFinal) {
          textarea.value += e.results[i][0].transcript;
        }
    }
}

const toggleSpeechRecognition = () => {
    if (recognizing) {
        recognition.stop();
        reset();
      } else {
        recognition.start();
        recognizing = true;
        document.querySelector('#mic-status').innerHTML = 'Click to Stop'
    }
}
