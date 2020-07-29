import tkinter as tk

from midiHandler import *

class homePage(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        splash = tk.Label(self, text = "Welcome to Pyano! \n The Simple MIDI Piano written in Python")
        
        image = tk.PhotoImage(file = ".\\Resources\\Piano_Keyboard.gif")
        keys = tk.Label(self, image=image)
        keys.image = image

        splash.pack()
        keys.pack()

class settingsPage(tk.Frame):
    
    def __init__(self, parentWindow, *args, **kwargs):
        super().__init__(*args, **kwargs)

        mh = midiHandler()

        settingsPage = tk.Frame(parentWindow)
        
        inputsList = ["Select an option"] + mh.listMidiInputs()
        
        inputVal = tk.StringVar(settingsPage)
        inputVal.set(inputsList[0])
        inputSelection = tk.OptionMenu(
            settingsPage, 
            inputVal, 
            *inputsList, 
            command = mh.selectInput)
        
        inputSelection.pack()
        settingsPage.pack()
        
