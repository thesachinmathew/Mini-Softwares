from flask import Flask, request, send_file, jsonify
from pydub import AudioSegment
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Replace this with your actual API key
API_KEY = 'your-api-key-here'

def check_api_key(key):
    return key == API_KEY

@app.route('/convert', methods=['POST'])
def convert_audio():
    api_key = request.headers.get('Authorization')
    if not api_key or not check_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_extension = file.filename.rsplit('.', 1)[1].lower()
    if file_extension not in ['wav', 'mp3', 'ogg']:
        return jsonify({'error': 'Unsupported file type'}), 400

    filename = f"{uuid.uuid4()}.{file_extension}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Convert to a different format (e.g., MP3)
    output_filename = f"{uuid.uuid4()}.mp3"
    output_filepath = os.path.join(CONVERTED_FOLDER, output_filename)
    
    audio = AudioSegment.from_file(filepath)
    audio.export(output_filepath, format="mp3")

    return send_file(output_filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
