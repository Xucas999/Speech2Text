import pyaudio,vosk,subprocess,json
import main,AudioIn as ain

import ipywidgets as widgets
from IPython.display import display

from threading import Thread
from queue import Queue
from vosk import Model, KaldiRecognizer

model = Model(model_name="vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, ain.FRAME_RATE)
rec.SetWords(True)

def speech_recognition(output):
    while not main.messages.empty():
        frames = main.recordings.get()

        rec.AcceptWaveform(b''.join(frames))
        result = rec.Result()
        text = json.loads(result)["text"]

        cased = subprocess.check_output("python recasepunc/recasepunc.py predict recasepunc/checkpoint", shell=True, text=True,input=text)
