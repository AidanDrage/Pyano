import tkinter as tk

import HomePage as hp
import SetingsPage as sp

class MenuBar(tk.Menu):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.add_command(label="Home",
            command = lambda: self.master.change_page(hp.HomePage(self.master)))
        
        self.add_command(label="Settings",
            command = lambda: self.master.change_page(sp.SettingsPage(self.master)))


        #menubar.add_command(label="Home", 
            #command = lambda: self.change_page(hp.HomePage(self)))
        #menubar.add_command(label="Settings", 
            #command = lambda: self.change_page(sp.SettingsPage(self)))
        