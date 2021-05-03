import tkinter
from tkinter import ttk


# def button1_click():
#     print('ok')

root = tkinter.Tk()

button1 = tkinter.Button(root, text = 'button1')
button1.config(command = lambda:button1_click())
button1.grid()

button1.invoke()
# button1.invoke()


root.mainloop()