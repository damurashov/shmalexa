"""
Credits:
- https://medium.com/@nimritakoul01/offline-speech-to-text-in-python-f5d6454ecd02
- narrakeet.com for beautiful voices
"""

import json
import os
import pathlib
import pyaudio
import shmalexa.voice.play
import tired.fs
import vosk
import sys
import importlib

ACTIVATE_PHRASE = "hey babe"
DEACTIVATE_PHRASE = "never mind"
DEBUG = os.environ.get("DEBUG", False)
VERBOSE = os.environ.get("VERBOSE", False)
LOG = os.environ.get("LOG", False)
SCRIPTS_DIR = os.environ.get("SCRIPTS", pathlib.Path.home() / ".local" / "shmalexa")


def command(text):
    scripts_dir = pathlib.Path(SCRIPTS_DIR).resolve()
    print("Using scripts from", str(scripts_dir))
    here_dir = pathlib.Path(__file__).resolve().parent
    sys.path.append(scripts_dir)
    scripts_dir = os.path.relpath(str(scripts_dir), here_dir)
    print(scripts_dir)
    scripts = tired.fs.find(str(scripts_dir) + "/*.py", is_file=True)
    for script in scripts:
        script = script.resolve()
        module = importlib.import_module(script.stem)
        print(module.__dir__())
        function = getattr(module, "shmalexa")
        try:
            if function(text):
                return True
            else:
                return False
        except Exception:
            print("failed to execute script")
    return False


def main():
    # model_path = "../models/vosk-model-en-us-0.42-gigaspeech"
    # model_path = "../models/vosk-model-en-us-0.42-gigaspeech"
    here = pathlib.Path(__file__).resolve().parent
    model_path = str(here / "models" / "vosk-model-small-en-us-0.15")
    # model_path = "../models/vosk-model-en-us-daanzu-20200905-lgraph"
    # model_path = "../models/vosk-model-en-us-0.22"
    # model_path = "./models/vosk-model-en-us-daanzu-20200905"
    model = vosk.Model(model_path)

    # Create a recognizer
    rec = vosk.KaldiRecognizer(model, 16000)

    # Open the microphone stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8192)

    output_file_path = "recognized_text.txt"

    expect_input = False
    with open(output_file_path, "w") as output_file:
        print("Listening for speech. Say 'Terminate' to stop.")
        # Start streaming and recognize speech
        while True:
            data = stream.read(4096) #read in chunks of 4096 bytes
            if rec.AcceptWaveform(data): #accept waveform of input voice
                # Parse the JSON result and get the recognized text
                result = json.loads(rec.Result())
                recognized_text = result['text']

                if len(recognized_text.strip()) == 0:
                    continue

                # Write recognized text to the file
                if LOG:
                    output_file.write(recognized_text + "\n")
                if VERBOSE:
                    print(recognized_text)

                # Check for keyword
                if "terminate" in recognized_text.lower():
                    stream.stop_stream()
                    shmalexa.voice.play.play("terminate")
                    stream.start_stream()
                    break
                elif ACTIVATE_PHRASE in recognized_text.lower():
                    stream.stop_stream()
                    shmalexa.voice.play.play("activate")
                    stream.start_stream()
                    expect_input = True
                    # data = stream.read(4096) # flush stream, crutch
                elif expect_input:
                    if DEACTIVATE_PHRASE in recognized_text.lower():
                        stream.stop_stream()
                        shmalexa.voice.play.play("deactivate")
                        expect_input = False
                        stream.start_stream()
                    elif not command(recognized_text.lower()):
                        stream.stop_stream()
                        shmalexa.voice.play.play("mismatch")
                        stream.start_stream()
                    else:
                        shmalexa.voice.play.play("affirmative")
                        expect_input = False
                    

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PyAudio object
    p.terminate()

