import tkinter as tk

import MenuBar as mb
import HomePage as hp
import SetingsPage as sp
        
class PyanoApp(tk.Tk):

    global currentpage 
    global listnerThread
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(menu=mb.MenuBar())
        
        global currentpage 
        currentpage = hp.HomePage(self)
        currentpage.pack()

    def change_page(self, newpage):
        global currentpage
        currentpage.pack_forget()
            
        currentpage = newpage
        newpage.pack()

app = PyanoApp()
app.mainloop()