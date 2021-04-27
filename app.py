import tkinter
from tkinter import ttk



figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
naipes_list = [('d','#014082'), ('h','#CC0000'), ('s','#000000'), ('c','#00732B')]
cards_matrix = [[figure + naipe[0] for figure in figures_list] for naipe in naipes_list]



class PokerRangeAnalysis:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_resizable(False, False) # block window resize
        self.root.title('Poker Range Analysis')
        self.create_tabs_layout()

    def create_tabs_layout(self):
        tabs_control = ttk.Notebook(self.root)
        tabs_control.grid(padx = 5, pady = 5)

        # Tab Start
        tab_start = ttk.Frame(tabs_control, width = 546, height = 210)
        tabs_control.add(tab_start, text="Início")

        #  Tab Start - Frame Basic Informations
        label_frame = tkinter.LabelFrame(tab_start, text = "Informações Básicas", 
            width = 258, height = 78, padx = 10, pady = 5)
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

        #  Tab Start - Frame Opponent Informations
        label_frame = tkinter.LabelFrame(tab_start, text = "Informações do Vilão", 
            width = 258, height = 78, padx = 10, pady = 5)
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

        #  Tab Start - Frame Notes And Infos
        label_frame = tkinter.LabelFrame(tab_start, text = "Notes e Infos", 
            width = 258, height = 100, padx = 5, pady = 10)
        label_frame.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = 'we')

        label_notes = tkinter.Label(label_frame, text = 'Notes')
        label_notes.grid(row = 0, column = 0, sticky = 'w')

        textbox_notes = tkinter.Text(label_frame, width = 35, height = 3)
        textbox_notes.grid(row = 1, column = 0, padx = 5)

        label_infos = tkinter.Label(label_frame, text = 'Infos')
        label_infos.grid(row = 0, column = 1, sticky = 'w')

        textbox_infos = tkinter.Text(label_frame, width = 35, height = 3)
        textbox_infos.grid(row = 1, column = 1, padx = 5)


        # Streets tabs
        street_tabs_structure = {
            'Pré-Flop': {'tab_name': 'PF', 'qtd': 2}, 'Flop': {'tab_name': 'F', 'qtd': 3}, 
            'Turn': {'tab_name': 'T', 'qtd': 3}, 'River': {'tab_name': 'R', 'qtd': 3}}

        for street in street_tabs_structure:
            main_frame = tkinter.Frame()
            path = street_tabs_structure[street]
            self.creates_slot_buttons(main_frame, street , path['qtd'], path['tab_name'], 0, 0)
            self.creates_equity_frame(main_frame, path['qtd'], 'equity', 0, 1)
            self.creates_equity_frame(main_frame, path['qtd'], 'fold_equity', 0, 2)
            self.creates_cards_seletion_frame(self.root, 1, 0)
            tabs_control.add(main_frame, text = street)
    
    def creates_slot_buttons(self, frame:object, street:str, qtd:str, abbreviation:str, row:str, column:str):
        buttons_frame = tkinter.Frame(frame)
        buttons_frame.grid(row = row, column = column, sticky = 's', ipady = 7)

        for n in range(qtd):
            slot_button_name = f'{abbreviation}{n + 1}'
            slot_button = tkinter.Button(buttons_frame, text = slot_button_name, width = 10)
            slot_button.grid(row = n, column = 0, padx = 5, pady = 5, sticky = 's')

    def creates_equity_frame(self, frame:object, entry_rows:str, equity_type:str, frame_row:str, frame_column:str):
        '''creates the equity and fold equity frames on each street'''
        
        equity_labels_dict = {
            'equity': ['Range\n(mãos)', 'Eq. Hero\n(%)', 'Eq. Vilao\n(%)', 'Split\n(%)'],
            'fold_equity': ['FE/Block\n(mãos)', 'FE/Block\n(%)', 'Cbet\n(%)'],}

        equity_frame = tkinter.Frame(frame, padx = 5, pady = 5, bd = 2, relief = 'groove')
        equity_frame.grid(row = frame_row, column = frame_column, padx = 10, pady = 10)

        for i in range(len(equity_labels_dict[equity_type])):
            label = tkinter.Label(equity_frame, text = equity_labels_dict[equity_type][i])
            label.grid(row = 0, column = i, padx = 5)

            # create the FALSE entries
            for x in range(entry_rows):
                false_label = tkinter.Label(equity_frame, width = 8, relief = 'groove', bg = 'white')
                false_label.grid(row = x + 1, column = i, padx = 5, pady = 7)

    def creates_cards_seletion_frame(self, frame:object, row:str, column:str):
        '''creates the frame for selecting the hero cards and each street'''
        
        main_frame = tkinter.Frame(frame, padx = 5, pady = 5, bd = 2, relief = 'groove')
        main_frame.grid(row = row, column = column, padx = 10, pady = 10, columnspan = 3)

        list_labels = ['Hero', 'Flop', 'Turn', 'River']
        img_cards = tkinter.PhotoImage(file = 'icons/card_selection.png')
        img_clear = tkinter.PhotoImage(file = 'icons/button_clear.png')

        for i in range(len(list_labels)):
            owner_cards = list_labels[i]

            frame = tkinter.Frame(main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{owner_cards}:')
            label.grid(row = 0, column = 0)

            entry = tkinter.Entry(frame, width = 8)
            entry.grid(row = 0, column = 1, padx = 5)

            choose_cards_button = tkinter.Button(frame, image = img_cards)
            choose_cards_button.image = img_cards  # Keep a reference
            choose_cards_button.grid(row = 0, column = 2, padx = 5, pady = 5)
            choose_cards_button.config(command = lambda owner_cards = owner_cards : self.open_card_selection_window(owner_cards))

            clear_button = tkinter.Button(frame, image = img_clear)
            clear_button.image = img_clear  # keep a reference
            clear_button.grid(row = 0, column = 3)

    def show(self):
        self.root.mainloop()

    def open_card_selection_window(self, owner_cards):
        if owner_cards == 'Hero':
            hero_card_selection.show()
        elif owner_cards == 'Flop':
            flop_card_selection.show()
        elif owner_cards == 'Turn':
            turn_card_selection.show()
        else:
            river_card_selection.show()


class CardSelectionWindow:
    def __init__(self, owner_cards:str):
        self.owner_cards = owner_cards
        self.wcs = tkinter.Toplevel()
        self.wcs.title(f'Seleção de cartas - {self.owner_cards}')
        # self.wcs.wm_resizable(False, False)
        self.wcs.withdraw() # start hidden
        self.wcs.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_clicked())
        self.create_layout()

    def create_layout(self):
        main_frame = tkinter.Frame(self.wcs)
        main_frame.grid()

        cards_frame = tkinter.Frame(main_frame)
        cards_frame.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        for row in range(4):
            for col in range(13):
                card_button_name = cards_matrix[row][col]
                card_button_color = naipes_list[row][1]
                Cards(card_button_name, card_button_color, cards_frame, row, col).create_card_button()  

        ok_button = tkinter.Button(main_frame, text = 'OK', width = 6, state = 'disabled')
        ok_button.grid(row = 1, column = 0, pady = 5)

        cancel_button = tkinter.Button(main_frame, text = 'Cancel', width = 6)
        cancel_button.grid(row = 1, column = 1, pady = 5)     

    def show(self):
        self.wcs.deiconify()

    def cancel_button_clicked(self):
        self.wcs.withdraw()


class Cards:
    def __init__(self, card_name:str, card_color:str, frame:object, row: str, column:str):
        self.card_name = card_name
        self.card_color = card_color
        self.frame = frame
        self.row = row
        self.column = column

    def create_card_button(self):
        card_button = tkinter.Button(self.frame, width = 2, heigh = 2, text = self.card_name, fg = self.card_color, relief = 'groove')
        card_button.grid(row = self.row, column = self.column)
        card_button.config(command = lambda: self.card_button_clicked(card_button))
    
    def card_button_clicked(self, card_button:object):
        card_button['bg'] = 'gray'
        
        
app = PokerRangeAnalysis()

# creates the four cards selection windows
hero_card_selection = CardSelectionWindow('hero')
flop_card_selection = CardSelectionWindow('flop')
turn_card_selection = CardSelectionWindow('turn')
river_card_selection = CardSelectionWindow('river')



if __name__ == '__main__':
    app.show()