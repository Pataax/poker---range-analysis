import tkinter
from tkinter.constants import W


class Window:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.dict = {}
        self.create_layout()
    
    def create_layout(self):
        self.b = tkinter.Button(command = self.button_click)
        self.b.grid()

    def button_click(self):
        print('ok')

    def show(self):
        self.root.mainloop()

w = Window()
# w.b['state'] = 'disabled'
w.b.unbind(w.button_click)
# w.b.invoke()
w.show()

