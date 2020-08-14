import tkinter as tk

class HomePage(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        splash = tk.Label(self, text = "Welcome to Pyano! \n The Simple MIDI Piano written in Python")
        
        image = tk.PhotoImage(file = ".\\Resources\\Piano_Keyboard.gif")
        keys = tk.Label(self, image=image)
        keys.image = image

        splash.pack()
        keys.pack()