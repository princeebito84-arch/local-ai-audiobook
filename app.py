from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import tempfile
from generator import generate_story
from tts import synthesize_speech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    idea = request.form.get('idea', '').strip()
    title = request.form.get('title', '').strip() or 'Untitled'
    length = int(request.form.get('length', 600))
    voice = request.form.get('voice', 'default')

    if not idea:
        return redirect(url_for('index'))

    # Generate story text
    story = generate_story(idea, title=title, max_tokens=length)

    # Synthesize to a temporary file
    tmp_dir = tempfile.mkdtemp()
    out_wav = os.path.join(tmp_dir, 'audiobook.wav')
    out_mp3 = os.path.join(tmp_dir, 'audiobook.mp3')

    synthesize_speech(story, out_wav, voice=voice, convert_mp3=True, mp3_path=out_mp3)

    return send_file(out_mp3, as_attachment=True, download_name=f"{title}.mp3")

if __name__ == '__main__':
    app.run(debug=True)
