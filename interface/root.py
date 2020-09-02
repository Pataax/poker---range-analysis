import tkinter
from tkinter import ttk


from tab_start import FrameBasicInformations, FrameOpponentInformations, FrameNotesAndInfos
from objects import FrameCards, FrameStreetsButtons, FrameStreetsTable, RangeWindow


class PokerRangeAnalysis:
    def __init__(self, master):
        self.master = master
        self.master.title('Poker Range Analysis')
        self.creates_tab_control(master)

    def creates_tab_control(self, master):
        tab_control = ttk.Notebook(master)
        tab_control.grid(padx = 5, pady = 5)
        self.creates_tabs_layout(tab_control)

    def creates_tabs_layout(self, master):
        tab_start = ttk.Frame(root, width = 546, height = 210)
        master.add(tab_start, text="Início")
        FrameBasicInformations(tab_start)
        FrameOpponentInformations(tab_start)
        FrameNotesAndInfos(tab_start)

        streets = {'Pré-Flop': ('PF', 2), 'Flop': ('F', 3), 'Turn': ('T', 3), 'River': ('R', 3)}
        buttons = {}
        for key, value in streets.items():
            main_frame = tkinter.Frame()
            # used to center on the main_frame - don't work in class
            # inside_frame = tkinter.Frame(main_frame, bg = 'red') 
            # inside_frame.place(in_=main_frame, anchor="c", relx=.5, rely=.5)
            FrameStreetsButtons(main_frame, value[1], value[0], 0, 0)
            buttons[key] = FrameStreetsButtons(main_frame, value[1], value[0], 0, 0)
            FrameStreetsTable(main_frame, value[1], 'equity', 0, 1)
            FrameStreetsTable(main_frame, value[1], 'fold_equity', 0, 2)
            FrameCards(main_frame, 1, 0)
            master.add(main_frame, text = key)

if __name__ == '__main__':
    root = tkinter.Tk()
    PokerRangeAnalysis(root)
    root.mainloop()

# buttons["Pré-Flop"].buttons_dict["PF1"].config(state = 'disabled')
