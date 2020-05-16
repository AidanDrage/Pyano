import threading

import mido
from playsound import playsound


def listMidiInputs():
    return mido.get_input_names()

def selectInput(inputDevice):
    listenerThread = threading.Thread(target= lambda: midiListner(inputDevice))
    listenerThread.setDaemon(True)
    listenerThread.start()

def midiListner(inputDevice):
    if (inputDevice == "Select an option"):
        return
    else:
        input = mido.open_input(inputDevice)
        for msg in input:
            print(msg)
            if (msg.type is "note_on"):
                playsound(
                    ".\Resources\piano-ff-040-MiddleC - midi 60.wav", 
                    block = False
                    )
