import threading

import mido
from playsound import playsound

def getInputs():
    return mido.get_input_names()

def onClick(inputDevice):
    listenerThread = threading.Thread(
        target= lambda: midiListner(inputDevice))
    listenerThread.setDaemon(True)
    listenerThread.start()

def play():
    playsound("D:\Projects\Python\Pyano\Resources\piano-ff\piano-ff-001.wav")

def midiListner(inputDevice):
    if (inputDevice == "Select an option"):
        return
    else:
        i = mido.open_input(inputDevice)
        for msg in i:
            print(msg)
            play()