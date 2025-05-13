from flask import Flask, request, jsonify
from gtts import gTTS
from playsound import playsound
import os
import uuid

app = Flask(__name__)

@app.route('/speak', methods=['POST'])
def speak_text():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" in request'}), 400

    text = data['text']
    filename = f"{uuid.uuid4()}.mp3"

    try:
        tts = gTTS(text)
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
        return jsonify({'message': 'Text played successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
