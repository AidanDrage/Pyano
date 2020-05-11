import mido
from tkinter import *
import threading

def onClick(inputDevice):
    threading.Thread(target= lambda: midiListner(inputDevice)).start()

def midiListner(inputDevice):
    i = mido.open_input(inputDevice)
    for msg in i:
      print(msg)

window = Tk()

inputsList = ["Select an option"] + mido.get_input_names()
inputVal = StringVar(window)
inputVal.set(inputsList[0]) # default value
inputSelection = OptionMenu(window, inputVal, *inputsList, command = onClick)
inputSelection.pack()

window.mainloop()