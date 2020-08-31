import tkinter
from tkinter import ttk


from tab_start import FrameBasicInformations, FrameOpponentInformations, FrameNotesAndInfos
from objects import FrameCards, FrameStreetsButtons, FrameStreetsTable


# main window
root = tkinter.Tk()
root.title("Poker - Análise de Ranges")
# root.wm_geometry("500x330")
# root.wm_resizable("False", "False")


# tabcontrol
tabcontrol = ttk.Notebook(root)
tabcontrol.grid(padx = 5, pady = 5)

tab_start = ttk.Frame(root, width = 546, height = 210)
tabcontrol.add(tab_start, text="Início")
frame_basic_informations = FrameBasicInformations(tab_start)
frame_opponent_informations = FrameOpponentInformations(tab_start)
frame_notes_and_infos = FrameNotesAndInfos(tab_start)

streets = ('Pré-Flop', 2), ('Flop', 3), ('Turn', 3), ('River', 3)
for tab, row in streets:
    # frame = ttk.Frame(tabcontrol)
    main_frame = tkinter.Frame(tabcontrol)
    inside_frame = tkinter.Frame(main_frame)
    FrameStreetsButtons(inside_frame, row, 'F', 0, 0)
    FrameStreetsTable(inside_frame, row, 'equity', 0, 1)
    FrameStreetsTable(inside_frame, row, 'fold_equity', 0, 2)
    FrameCards(inside_frame, 1, 0)
    inside_frame.place(in_=main_frame, anchor="c", relx=.5, rely=.5)
    tabcontrol.add(main_frame, text = tab)


root.mainloop()
