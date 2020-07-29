import tkinter as tk

from pages import *
        
class PyanoApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.geometry("500x200")

        menubar = tk.Menu(self)
        menubar.add_command(label="Settings", command = lambda: settingsPage(self.master))
        self.config(menu=menubar)
        
        contents = homePage(self)
        contents.pack()

app = PyanoApp()
app.mainloop()