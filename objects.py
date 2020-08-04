from tkinter import *


class FrameBasicInformations:
    
    def __init__(self, master):
        label_frame = LabelFrame(master, text = "Informações Básicas", width = 258, height = 78, padx = 10, pady = 5)
        label_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        label_data = Label(label_frame, text="Data: ", justify = LEFT)
        entry_data = Entry(label_frame, width = 11)
        
        label_hora = Label(label_frame, text="Hora: ")
        entry_hora = Entry(label_frame, width = 8)
        
        label_torneio = Label(label_frame, text="Torneio: ", justify = LEFT)
        entry_torneio = Entry(label_frame)
        
        label_blinds = Label(label_frame, text="Blinds: ")
        entry_blinds = Entry(label_frame, width = 8)
        
        label_data.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = W)
        entry_data.grid(row = 0, column = 1, padx = 0, pady = 5, sticky = W)
        
        label_hora.grid(row = 0, column = 2, padx = 0, pady = 0, sticky = W)
        entry_hora.grid(row = 0, column = 3, padx = 0, pady = 0, sticky = W)

        label_torneio.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = W)
        entry_torneio.grid(row = 1, column = 1, padx = 0, pady = 5, sticky = W)

        label_blinds.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = W)
        entry_blinds.grid(row = 1, column = 3, padx = 0, pady = 0, sticky = W)


class FrameOpponentInformations:
    
    def __init__(self, master):
        label_frame = LabelFrame(master, text = "Informações do Vilão", width = 258, height = 78, padx = 10, pady = 5)
        label_frame.grid(row = 0, column = 1, padx = 1, pady = 10)

        label_position = Label(label_frame, text="Posição: ")
        entry_position = Entry(label_frame, width = 3)
        
        label_stack = Label(label_frame, text="Stack: ")
        entry_stack = Entry(label_frame, width = 5)
        
        label_vpip_pfr = Label(label_frame, text="VPIP/PFR: ")
        entry_vpip_pfr = Entry(label_frame, width = 8)
        
        label_style = Label(label_frame, text="Estilo: ")
        entry_style = Entry(label_frame)
        
        label_hands = Label(label_frame, text="Hands: ")
        entry_hands = Entry(label_frame, width = 8)
        
        label_position.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = W)
        entry_position.grid(row = 0, column = 1, padx = 0, pady = 5, sticky = W)
        
        label_stack.grid(row = 0, column = 2, padx = 0, pady = 0, sticky = W)
        entry_stack.grid(row = 0, column = 3, padx = 0, pady = 0, sticky = W)
        
        label_vpip_pfr.grid(row = 0, column = 4, padx = 0, pady = 0, sticky = W)
        entry_vpip_pfr.grid(row = 0, column = 5, padx = 0, pady = 0, sticky = W)

        label_style.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = W)
        entry_style.grid(row = 1, column = 1, padx = 0, pady = 5, sticky = W, columnspan = 3)

        label_hands.grid(row = 1, column = 4, padx = 0, pady = 0, sticky = W)
        entry_hands.grid(row = 1, column = 5, padx = 0, pady = 0, sticky = W)