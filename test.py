from tkinter import *


def clear():
    my_text.delete(1.0, END)

root = Tk()
root.title("Titulo da janela")

def get_text():
    my_label.config(text = my_text.get(1.0, END))


my_text = Text(root, 
               width = 60, 
               height = 10,
            #    font = ('helvetica', 16)
               )
my_text.pack(padx = 10, pady = 10)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text = 'Clear Screen', command = clear)
clear_button.grid(row = 0, column = 0, pady = 10)

get_text_button = Button(button_frame, text = 'Get Text', command = get_text)
get_text_button.grid(row = 0, column = 1, padx = 20)

my_label = Label(root, text = '')
my_label.pack(pady = 10)


root.mainloop()