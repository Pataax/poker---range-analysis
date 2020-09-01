import tkinter
from tkinter import ttk


from tab_start import FrameBasicInformations, FrameOpponentInformations, FrameNotesAndInfos
from objects import FrameCards, FrameStreetsButtons, FrameStreetsTable, RangeWindow


# main window
root = tkinter.Tk()
root.title("Poker - Análise de Ranges")
# root.wm_geometry("500x330")
# root.wm_resizable("False", "False")


# create tabcontrol
tabcontrol = ttk.Notebook(root)
tabcontrol.grid(padx = 5, pady = 5)


# layout tabs
tab_start = ttk.Frame(root, width = 546, height = 210)
tabcontrol.add(tab_start, text="Início")
frame_basic_informations = FrameBasicInformations(tab_start)
frame_opponent_informations = FrameOpponentInformations(tab_start)
frame_notes_and_infos = FrameNotesAndInfos(tab_start)

streets = {'Pré-Flop': ('PF', 2), 'Flop': ('F', 3), 'Turn': ('T', 3), 'River': ('R', 3)}
buttons = {}
for key, value in streets.items():
    # frame = ttk.Frame(tabcontrol)
    main_frame = tkinter.Frame(tabcontrol)
    inside_frame = tkinter.Frame(main_frame) # utilizado pra centralizar o frame na janela
    FrameStreetsButtons(inside_frame, value[1], value[0], 0, 0)
    buttons[key] = FrameStreetsButtons(inside_frame, value[1], value[0], 0, 0)

    FrameStreetsTable(inside_frame, value[1], 'equity', 0, 1)
    FrameStreetsTable(inside_frame, value[1], 'fold_equity', 0, 2)
    FrameCards(inside_frame, 1, 0)
    inside_frame.place(in_=main_frame, anchor="c", relx=.5, rely=.5)
    tabcontrol.add(main_frame, text = key)

buttons["Pré-Flop"].buttons_dict["PF1"].config(state = 'disabled')

root.mainloop()
