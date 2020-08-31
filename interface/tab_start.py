import tkinter


class FrameBasicInformations:
    
    def __init__(self, master):
        label_frame = tkinter.LabelFrame(master, text = "Informações Básicas", width = 258, height = 78, padx = 10, pady = 5)
        label_frame.grid(row = 0, column = 0, padx = 5, pady = 10)

        label_data = tkinter.Label(label_frame, text="Data: ", justify = 'left')
        entry_data = tkinter.Entry(label_frame, width = 11)
        
        label_hora = tkinter.Label(label_frame, text="Hora: ")
        entry_hora = tkinter.Entry(label_frame, width = 8)
        
        label_torneio = tkinter.Label(label_frame, text="Torneio: ", justify = 'left')
        entry_torneio = tkinter.Entry(label_frame)
        
        label_blinds = tkinter.Label(label_frame, text="Blinds: ")
        entry_blinds = tkinter.Entry(label_frame, width = 8)
        
        label_data.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = 'w')
        entry_data.grid(row = 0, column = 1, padx = 0, pady = 5, sticky = 'w')
        
        label_hora.grid(row = 0, column = 2, padx = 0, pady = 0, sticky = 'w')
        entry_hora.grid(row = 0, column = 3, padx = 0, pady = 0, sticky = 'w')

        label_torneio.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = 'w')
        entry_torneio.grid(row = 1, column = 1, padx = 0, pady = 5, sticky = 'w')

        label_blinds.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = 'w')
        entry_blinds.grid(row = 1, column = 3, padx = 0, pady = 0, sticky = 'w')


class FrameOpponentInformations:
    
    def __init__(self, master):
        label_frame = tkinter.LabelFrame(master, text = "Informações do Vilão", width = 258, height = 78, padx = 10, pady = 5)
        label_frame.grid(row = 0, column = 1, padx = 5, pady = 10)

        label_position = tkinter.Label(label_frame, text="Posição: ")
        entry_position = tkinter.Entry(label_frame, width = 3)
        
        label_stack = tkinter.Label(label_frame, text="Stack: ")
        entry_stack = tkinter.Entry(label_frame, width = 5)
        
        label_vpip_pfr = tkinter.Label(label_frame, text="VPIP/PFR: ")
        entry_vpip_pfr = tkinter.Entry(label_frame, width = 8)
        
        label_style = tkinter.Label(label_frame, text="Estilo: ")
        entry_style = tkinter.Entry(label_frame)
        
        label_hands = tkinter.Label(label_frame, text="Hands: ")
        entry_hands = tkinter.Entry(label_frame, width = 8)
        
        label_position.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = 'w')
        entry_position.grid(row = 0, column = 1, padx = 0, pady = 5, sticky = 'w')
        
        label_stack.grid(row = 0, column = 2, padx = 0, pady = 0, sticky = 'w')
        entry_stack.grid(row = 0, column = 3, padx = 0, pady = 0, sticky = 'w')
        
        label_vpip_pfr.grid(row = 0, column = 4, padx = 0, pady = 0, sticky = 'w')
        entry_vpip_pfr.grid(row = 0, column = 5, padx = 0, pady = 0, sticky = 'w')

        label_style.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = 'w')
        entry_style.grid(row = 1, column = 1, padx = 0, pady = 5, sticky = 'w', columnspan = 3)

        label_hands.grid(row = 1, column = 4, padx = 0, pady = 0, sticky = 'w')
        entry_hands.grid(row = 1, column = 5, padx = 0, pady = 0, sticky = 'w')

class FrameNotesAndInfos:
    
    def __init__(self, master):
        label_frame = tkinter.LabelFrame(master, text = "Notes e Infos", width = 258, height = 100, padx = 5, pady = 10)
        label_frame.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = 'we')

        label_notes = tkinter.Label(label_frame, text = 'Notes')
        label_notes.grid(row = 0, column = 0, sticky = 'w')

        textbox_notes = tkinter.Text(label_frame, width = 35, height = 3)
        textbox_notes.grid(row = 1, column = 0, padx = 5)

        label_infos = tkinter.Label(label_frame, text = 'Infos')
        label_infos.grid(row = 0, column = 1, sticky = 'w')

        textbox_infos = tkinter.Text(label_frame, width = 35, height = 3)
        textbox_infos.grid(row = 1, column = 1, padx = 5)
