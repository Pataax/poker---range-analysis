import tkinter

def cria_toplevel():
    window_card_selection = tkinter.Toplevel()
    window_card_selection.title(f'Seleção de cartas')
    window_card_selection.wm_resizable(False, False)

cria_toplevel()