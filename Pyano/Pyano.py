from tkinter import *

from midiHandler import *

class settingsPage():
    
    def __init__(self, window):

        mh = midiHandler()   
        
        inputsList = ["Select an option"] + mh.listMidiInputs()
        
        inputVal = StringVar(window)
        inputVal.set(inputsList[0])
        inputSelection = OptionMenu(
            window, 
            inputVal, 
            *inputsList, 
            command = mh.selectInput)
        
        inputSelection.pack()

class pyanoUI:
    
    window = Tk()
    w = settingsPage(window)
    window.mainloop()

