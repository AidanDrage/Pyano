import tkinter as tk

from midiHandler import *

class homePage(tk.Frame):

    def __init__(self, window):

        homePage = tk.Frame(window, bg = "blue")
        splash = tk.Label(homePage, text = "Hello, Pyano!")
        settingsButton = tk.Button(window, text = "Settings", command = lambda: settingsPage(window))

        splash.pack() 
        settingsButton.pack()       
        homePage.pack()

class settingsPage(tk.Frame):
    
    def __init__(self, window):

        mh = midiHandler()

        settingsPage = tk.Frame(window)
        
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
        
