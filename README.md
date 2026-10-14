# Local AI Audiobook Creator (Starter)

This project provides a minimal, local audiobook creator that:
- Generates short stories from an idea or storyline using a local LLM if available (GPT4All) or a simple fallback generator.
- Synthesizes speech locally using pyttsx3 (offline TTS).

Important: To be "free with no usage limit" the app runs locally on your machine and uses local models or local TTS engines. Large local LLMs and high-quality TTS may require downloading model files and have significant CPU/GPU requirements.

Quick start
1. Clone the repo and switch to the branch `feature/local-audiobook-starter`.
2. Create a Python 3.10+ virtual environment and install requirements:

   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

3. (Optional) Install system dependency `ffmpeg` if you want MP3 conversion.

4. Run the app:

   python app.py

5. Open http://127.0.0.1:5000 in your browser, enter an idea or storyline and click "Create Audiobook". The app will produce a story and an audio file for download.

Notes
- Story generation:
  - If `gpt4all` is installed and a compatible model is available, the app will try to use it. You must download a GPT4All-style model and point the environment variable GPT4ALL_MODEL or place it in the default location used by the gpt4all package.
  - If no local LLM is available the app falls back to a simple template-based generator (works offline, but produces simpler output).
- TTS:
  - Uses `pyttsx3` for offline speech synthesis (cross-platform).
  - Optionally converts generated WAV to MP3 using `pydub` + `ffmpeg` if ffmpeg is installed.

Limitations & Licensing
- "Free with no usage limit" is achievable if you run everything locally, but some open-source model licenses may restrict use. Check the license of any model you download.
- Running large models may require significant disk space and compute.

Files in this branch:
- app.py - Flask web interface
- generator.py - story generation wrapper (gpt4all fallback)
- tts.py - local TTS wrapper
- requirements.txt - Python dependencies
- templates/index.html - simple UI
- README.md - this file

Enjoy. If you'd like, I can:
- Add support for other local LLM backends (llama.cpp, text-generation-webui)
- Add a CLI mode or batch export
- Improve voice quality by wiring Coqui TTS / Mozilla TTS

