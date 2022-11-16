# User-interfase
from tkinter import *
import tkinter as tk
import re
from model import WriteFile

window = None
new_dict = WriteFile()
count = len(new_dict)

def create():
    global window
    window = tk.Tk() 
    window.title("Справочник")
    window.geometry("400x700")
    window['bg'] = '#0a0a0a'

    frame1 = Frame(window)
    frame1.pack()
    
    window.mainloop()

create()
