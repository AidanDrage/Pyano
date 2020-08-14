import tkinter as tk

import HomePage as hp
import SetingsPage as sp
        
class PyanoApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.geometry("500x200")

        menubar = tk.Menu(self)
        menubar.add_command(label="Home", 
            command = lambda: change_page(hp.HomePage(self)))
        menubar.add_command(label="Settings", 
            command = lambda: change_page(sp.SettingsPage(self)))
        self.config(menu=menubar)
        
        global currentpage 
        currentpage = hp.HomePage(self)
        currentpage.pack()

        def change_page(newpage):
            global currentpage
            currentpage.pack_forget()
            
            currentpage = newpage
            newpage.pack()

app = PyanoApp()
app.mainloop()