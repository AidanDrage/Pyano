from tkinter import *

import midiHandler as mh


window = Tk()

inputsList = ["Select an option"] + mh.getInputs()

inputVal = StringVar(window)
inputVal.set(inputsList[0])

inputSelection = OptionMenu(
    window, 
    inputVal, 
    *inputsList, 
    command = mh.onClick)
inputSelection.pack()

window.mainloop()
