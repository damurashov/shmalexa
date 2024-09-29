import pathlib
import playsound

__HERE = pathlib.Path(__file__).resolve().parent
__VOICES = {
    "activate": str(__HERE / "activate-2.mp3"),
    "deactivate": str(__HERE / "deactivate-2.mp3"),
    "terminate": str(__HERE / "terminate-3.mp3"),
    "mismatch": str(__HERE / "mismatch-4.mp3"),
    "affirmative": str(__HERE / "affirmative-1-jennifer.mp3"
}

def play(key):
    if key in __VOICES:
        playsound.playsound(__VOICES[key], True)

