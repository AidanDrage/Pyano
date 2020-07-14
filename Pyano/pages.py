import tkinter as tk

from midiHandler import *

class homePage(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        homePage = tk.Frame(self)
        splash = tk.Label(homePage, text = "Hello, Pyano!")
        settingsButton = tk.Button(homePage, text = "Settings", command = lambda: settingsPage(self.master))

        splash.pack() 
        settingsButton.pack()       
        homePage.pack()

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
        
