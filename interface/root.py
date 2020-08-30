import tkinter
from tkinter import ttk

from tab_start import FrameBasicInformations, FrameOpponentInformations, FrameNotesAndInfos
from tab_pre_flop import FramePreFlopButtons, FramePreFlopEquity, FramePreFlopFoldEquity
from tab_flop import FrameFlopButtons, FrameFlopEquity, FrameFlopFoldEquity
from tab_turn import FrameTurnButtons, FrameTurnEquity, FrameTurnFoldEquity
from tab_river import FrameRiverButtons, FrameRiverEquity, FrameRiverFoldEquity


# main window
root = tkinter.Tk()
root.title("Poker - Análise de Ranges")
# root.wm_geometry("570x330")
root.wm_resizable("False", "False")


# tabcontrol
tabcontrol = ttk.Notebook(root)
tabcontrol.grid(padx = 5, pady = 5)

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
frame_basic_informations = FrameBasicInformations(tab_start)
frame_opponent_informations = FrameOpponentInformations(tab_start)
frame_notes_and_infos = FrameNotesAndInfos(tab_start)

frame_pre_flop_buttons = FramePreFlopButtons(tab_pre_flop)
frame_pre_flop_equity = FramePreFlopEquity(tab_pre_flop)
frame_pre_flop_fold_equity = FramePreFlopFoldEquity(tab_pre_flop)

frame_flop_buttons = FrameFlopButtons(tab_flop)
frame_flop_equity = FrameFlopEquity(tab_flop)
frame_flop_fold_equity = FrameFlopFoldEquity(tab_flop)

frame_turn_buttons = FrameTurnButtons(tab_turn)
frame_turn_equity = FrameTurnEquity(tab_turn)
frame_turn_fold_equity = FrameTurnFoldEquity(tab_turn)

frame_river_buttons = FrameRiverButtons(tab_river)
frame_river_equity = FrameRiverEquity(tab_river)
frame_river_fold_equity = FrameRiverFoldEquity(tab_river)



root.mainloop()
