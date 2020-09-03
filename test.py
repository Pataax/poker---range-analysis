import tkinter

root = tkinter.Tk()

def imprimir(text):
    print(text)

for i in range(3):
    button = tkinter.Button(width = 2, text = i + 1, command = lambda i=i : imprimir((i + 1) * 10))
    button.grid(padx = 100, pady = 10)


root.mainloop()