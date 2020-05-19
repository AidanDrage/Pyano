from tkinter import *

from midiHandler import *

class homePage:

    def __init__(self, window):

        homePage = Frame(window, bg = "blue")
        splash = Label(homePage, text = "Hello, Pyano!")
        settingsButton = Button(window, text = "Settings", command = lambda: settingsPage(window))

        splash.pack() 
        settingsButton.pack()       
        homePage.pack()

class settingsPage:
    
    def __init__(self, window):

        mh = midiHandler()

        settingsPage = Frame(window)
        
        inputsList = ["Select an option"] + mh.listMidiInputs()
        
        inputVal = StringVar(settingsPage)
        inputVal.set(inputsList[0])
        inputSelection = OptionMenu(
            settingsPage, 
            inputVal, 
            *inputsList, 
            command = mh.selectInput)
        
        inputSelection.pack()
        settingsPage.pack()
        
