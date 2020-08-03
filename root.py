from tkinter import *
from tkinter import ttk

from objects import FrameBasicInformations, FrameOpponentInformations


# main window
root = Tk()
root.title("Poker - Análise de Ranges")
# root.wm_geometry("570x330")
root.wm_resizable("False", "False")


# tabcontrol
tabcontrol = ttk.Notebook(root)
tabcontrol.grid(padx = 10, pady = 10)

tab_start = ttk.Frame(root, width = 546, height = 210)
tab_pre_flop = ttk.Frame(root, width = 546, height = 210)
tab_flop = ttk.Frame(root, width = 546, height = 210)
tab_turn = ttk.Frame(root, width = 546, height = 210)
tab_river = ttk.Frame(root, width = 546, height = 210)

tabcontrol.add(tab_start, text="Início")
tabcontrol.add(tab_pre_flop, text="Pré-Flop")
tabcontrol.add(tab_flop, text="Flop")
tabcontrol.add(tab_turn, text="Turn")
tabcontrol.add(tab_river, text="River")


# frames
frame_basic_informaitons = FrameBasicInformations(tab_start)
frame_opponent_informaitons = FrameOpponentInformations(tab_start)


root.mainloop()