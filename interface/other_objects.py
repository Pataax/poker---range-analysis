import tkinter


class FrameCards:

    def __init__(self, master, name, row, column, padx):
        self.name = name
        self.row = row
        self.column = column
        self.padx = padx


        frame = tkinter.Frame(master)
        frame.grid(row = self.row, column = self.column, padx = self.padx)

        label = tkinter.Label(frame, text = f'{self.name}:')
        label.grid(row = 0, column = 0)

        entry = tkinter.Entry(frame, width = 8)
        entry.grid(row = 0, column = 1, padx = 5)

        button_choose = tkinter.Button(frame, width = 2, height = 1)
        button_choose.grid(row = 0, column = 2, padx = 5, pady = 5)

        button_clear = tkinter.Button(frame, width = 2)
        button_clear.grid(row = 0, column = 3)
