from tkinter import *
from tkinter import ttk

root = Tk()
root.wm_geometry("500x500")


class FrameBasicInformation:

    def __init__(self, master):
        lf = LabelFrame(master, text = "text")
        lf.pack()

        b = Button(lf, text = "buttom")
        b.pack()

x = FrameBasicInformation(root)
root.mainloop()