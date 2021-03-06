import tkinter
from tkinter import ttk


from tab_start import FrameBasicInformations, FrameOpponentInformations, FrameNotesAndInfos
from objects import FrameStreetsSelectCards, FrameStreetsButtons, FrameStreetsEquity, WindowRangeSelection


class PokerRangeAnalysis:
    def __init__(self, master):
        self.master = master
        self.master.title('Poker Range Analysis')
        self.creates_tab_control(master)

    def creates_tab_control(self, master):
        self.tab_control = ttk.Notebook(master)
        self.tab_control.grid(padx = 5, pady = 5)
        self.creates_tabs_layout(self.tab_control)

    def creates_tabs_layout(self, master):
        tab_start = tkinter.Frame(root, width = 546, height = 210)
        self.tab_control.add(tab_start, text="Início")
        FrameBasicInformations(tab_start)
        FrameOpponentInformations(tab_start)
        FrameNotesAndInfos(tab_start)

        streets = {'Pré-Flop': ('PF', 2), 'Flop': ('F', 3), 'Turn': ('T', 3), 'River': ('R', 3)}
        # buttons = {}
        for key, value in streets.items():
            main_frame = tkinter.Frame()
            # used to center on the main_frame - don't work in class
            # inside_frame = tkinter.Frame(main_frame, bg = 'red') 
            # inside_frame.place(in_=main_frame, anchor="c", relx=.5, rely=.5)

            FrameStreetsButtons(main_frame, value[1], value[0], 0, 0)
            # buttons[key] = FrameStreetsButtons(main_frame, value[1], value[0], 0, 0)
            FrameStreetsEquity(main_frame, value[0], value[1], 'equity', 0, 1)
            FrameStreetsEquity(main_frame, value[0], value[1], 'fold_equity', 0, 2)
            FrameStreetsSelectCards(root, 1, 0)
            self.tab_control.add(main_frame, text = key)
    
        if self.tab_control.select(self.tab_control.index(0)):
            print

if __name__ == '__main__':
    root = tkinter.Tk()
    root.wm_resizable(False, False)
    PokerRangeAnalysis(root)
    root.mainloop()