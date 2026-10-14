import pyttsx3
import os
from pydub import AudioSegment

_engine = None

def _get_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        # Optional: tweak voice/rate here
        rate = _engine.getProperty('rate')
        _engine.setProperty('rate', max(120, rate - 20))
    return _engine


def synthesize_speech(text: str, out_wav_path: str, voice: str = 'default', convert_mp3: bool = False, mp3_path: str = None):
    """Synthesizes speech to WAV. Optionally convert to MP3 (requires ffmpeg) using pydub.

    Returns the path to the produced file (wav or mp3).
    """
    engine = _get_engine()
    # pyttsx3 saves to file by directing output via save_to_file
    engine.save_to_file(text, out_wav_path)
    engine.runAndWait()

    if convert_mp3 and mp3_path:
        # Convert WAV to MP3 using pydub (requires ffmpeg available on PATH)
        try:
            audio = AudioSegment.from_wav(out_wav_path)
            audio.export(mp3_path, format='mp3')
            return mp3_path
        except Exception:
            # If conversion fails, return WAV path
            return out_wav_path
    return out_wav_path
