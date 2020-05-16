import threading

import mido
from playsound import playsound

def listMidiInputs():
    return mido.get_input_names()

def selectInput(inputDevice):
    listenerThread = threading.Thread(
        target= lambda: midiListner(inputDevice))
    listenerThread.setDaemon(True)
    listenerThread.start()

def midiListner(inputDevice):
    if (inputDevice == "Select an option"):
        return
    else:
        input = mido.open_input(inputDevice)
        for msg in input:
            if (msg.type is "note_on"):
                playsound("D:\Projects\Python\Pyano\Resources\piano-ff\piano-ff-001.wav")