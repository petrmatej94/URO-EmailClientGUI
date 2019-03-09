from tkinter import font
from tkinter import *


def open_settings(root):
    window = Toplevel(root)
    window.grab_set()
    window.geometry("600x400")
    window.minsize(width=600, height=400)
    window.title('Settings')

    mainFrame = Frame(window, relief=GROOVE, border=2, bg="gray")
    mainFrame.pack(fill=BOTH, expand=1, side=TOP)