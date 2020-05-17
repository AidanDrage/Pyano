import threading

import mido
from playsound import playsound


class midiHandler:

    def listMidiInputs(self):
        return mido.get_input_names()

    def midiListner(self, inputDevice):
        if (inputDevice == "Select an option"):
            return
        else:
            input = mido.open_input(inputDevice)
            for msg in input:
                print(msg)
                if (msg.type is "note_on"):
                    self.playNote(msg)    

    def selectInput(self, inputDevice):
        listenerThread = threading.Thread(target= lambda: self.midiListner(inputDevice))
        listenerThread.setDaemon(True)
        listenerThread.start()

    def playNote(self, msg):
        playsound(
            ".\\Resources\\" + str(msg.note) + ".wav", 
            block = False
            )
