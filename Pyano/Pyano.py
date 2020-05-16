import midiHandler as mh

from tkinter import *

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
