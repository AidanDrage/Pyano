import tkinter as tk

from MIDIHandler import *

class SettingsPage(tk.Frame):
    
    def __init__(self, parentWindow, *args, **kwargs):
        super().__init__(*args, **kwargs)

        splash = tk.Label(self, text = "Settings!")
        splash.pack()

        mh = midiHandler()

        inputsList = ["Select an option"] + mh.listMidiInputs()
        inputVal = tk.StringVar(self)
        inputVal.set(inputsList[0])
        inputSelection = tk.OptionMenu(
            self, 
            inputVal, 
            *inputsList, 
            command = mh.selectInput)
    
        inputSelection.pack()