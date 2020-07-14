import tkinter as tk

from pages import *
        
class PyanoApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        contents = homePage(self)
        contents.pack()

app = PyanoApp()
app.mainloop()