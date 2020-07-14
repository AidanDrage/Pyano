import tkinter as tk

from pages import *
        
class pyanoUI(tk.Tk):
    
    window = tk.Tk()
    window.geometry("250x250")
    w = homePage(window)
    window.mainloop()

