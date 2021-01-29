import tkinter, itertools
from pprint import pprint


current_color_button_name = ''

selected_cards = {'Hero':[], 'Flop':[], 'Turn':[], 'River':[]}




removed_combinations = {}




streets_labels_dict = {}
streets_ranges_control = {}

# ----------------------------------------------------------------------------------------------------

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
        
class FrameStreetsSelectCards:
    def __init__(self, master, row, column):
        self.row = row
        self.column = column

        # main frame
        self.main_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        self.main_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10, columnspan = 3)

        labels_list = ['Hero', 'Flop', 'Turn', 'River']
        img_cards = tkinter.PhotoImage(file = 'interface/images/card_selection.png')
        img_clear = tkinter.PhotoImage(file = 'interface/images/button_clear.png')

        for i in range(len(labels_list)):
            label_name = labels_list[i]

            frame = tkinter.Frame(self.main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{label_name}:')
            label.grid(row = 0, column = 0)

            entry = tkinter.Entry(frame, width = 8)
            entry.grid(row = 0, column = 1, padx = 5)

            button_choose = tkinter.Button(frame, image = img_cards)
            button_choose.image = img_cards  # Keep a reference
            button_choose.grid(row = 0, column = 2, padx = 5, pady = 5)
            button_choose.config(command = lambda label_name = label_name, button_choose = button_choose, entry = entry: WindowCardSelection(label_name, button_choose, entry))
            button_clear = tkinter.Button(frame, image = img_clear, command = lambda entry = entry, button_choose = button_choose, label_name = label_name: self.clear_button_click(entry, button_choose, label_name))
            button_clear.image = img_clear  # keep a reference
            button_clear.grid(row = 0, column = 3)

    def clear_button_click(self, entry: object, button_choose: object, label_name:str):
        CardsAndHands().selected_card(label_name, add_card = '', del_card = entry.get())
        entry.delete(0, 'end')
        button_choose['state'] = 'active'
        # selected_cards[label_name] = []
        print(selected_cards)

class WindowCardSelection:
    def __init__(self, owner_cards:str, caller_button:object, entry:object) -> object:
        # streets_ranges_control['PF1']['range_detail']['RF+']['button']['text'] = 'y'
        '''Creates a window for selecting Hero, Flop, Turn and River cards'''
        self.owner_cards = owner_cards
        self.caller_button = caller_button
        self.caller_button['state'] = 'disabled'
        self.entry = entry
        self.create_gui(self.owner_cards)
        self.check_entry_filled(self.owner_cards, self.entry.get())

    def create_gui(self, owner_cards: str) -> object:
        '''Creates the window interface'''

        # creates the top level
        window_card_selection = tkinter.Toplevel()
        window_card_selection.title(f'Seleção de cartas - {owner_cards}')
        window_card_selection.wm_resizable(False, False)
        window_card_selection.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_click(window_card_selection, self.caller_button, self.entry, self.owner_cards))

        main_frame = tkinter.Frame(window_card_selection)
        main_frame.grid()

        # creates matrix of the card buttons
        cards_frame = tkinter.Frame(main_frame)
        cards_frame.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        self.card_button_dict = {}

        for row in range(4):
            for col in range(13):
                card_button_name = cards[row][col]
                card_button_color = naipes_list[row][1]

                card_button = tkinter.Button(cards_frame, width = 2, heigh = 2, text = card_button_name, fg = card_button_color, relief = 'groove')
                card_button.grid(row = row, column = col, padx = 1, pady = 1)
                card_button.config(command = lambda card_button_name = card_button_name: self.card_button_click(owner_cards, card_button_name))

                self.card_button_dict[card_button_name] = card_button
                
        # creates auxiliary buttons
        self.ok_button = tkinter.Button(main_frame, text = 'OK', width = 6, state = 'disabled', command = lambda: self.ok_button_click(window_card_selection, self.caller_button, self.entry, self.owner_cards))
        self.ok_button.grid(row = 1, column = 0, pady = 5)

        self.cancel_button = tkinter.Button(main_frame, text = 'Cancel', width = 6, command = lambda: self.cancel_button_click(window_card_selection, self.caller_button, self.entry, self.owner_cards))
        self.cancel_button.grid(row = 1, column = 1, pady = 5)

    def check_entry_filled(self, owner_cards:str, input_entry: str):
        '''Identifies whether you already have cards in the entry (added manually or previously selected)'''

        # extracts the list of cards from the current owner
        list_selected_cards = CardsAndHands().selected_card(owner_cards, input_entry) 
        if list_selected_cards:
            selected_cards[owner_cards] = []  # clears the list of cards and resends the command to select
            for card in list_selected_cards:
                self.card_button_click(owner_cards, card)
        # Identifies the cards already selected on the other streets and disables them
        for key in selected_cards:
            if key != owner_cards:
                for card in selected_cards[key]:
                    self.card_button_dict[card]['state'] = 'disabled'

    def manages_ok_button(self, owner_cards: str) -> bool:
        '''Check how many cards have already been selected for this 'owner' '''

        if owner_cards == 'Flop' and len(selected_cards[owner_cards]) == 3:
            self.ok_button['state'] = 'active'
            return False

        elif owner_cards == 'Turn' or owner_cards == 'River' and len(selected_cards[owner_cards]) == 1:
            self.ok_button['state'] = 'active'
            return False

        elif owner_cards == 'Hero' and len(selected_cards[owner_cards]) == 2:
            self.ok_button['state'] = 'active'
            return False

        else:
            self.ok_button['state'] = 'disabled'
            return True

    def card_button_click(self, owner_cards:str, card_button_name:str):
        '''Select and deselect cards if possible'''

        # checks the number of cards that have already been selected
        if owner_cards == 'Flop' and len(selected_cards[owner_cards]) == 3:
            permission = False
        elif (owner_cards == 'Turn' or owner_cards == 'River') and len(selected_cards[owner_cards]) == 1:
            permission = False
        elif owner_cards == 'Hero' and len(selected_cards[owner_cards]) == 2:
            permission = False
        else:
            permission = True
        
        # identifies the object (button) by name
        card_button = self.card_button_dict[card_button_name]

        if permission == True and card_button['bg'] == 'SystemButtonFace':
            card_button['bg'] = 'gray'
            CardsAndHands().selected_card(owner_cards, add_card = card_button['text'])
            self.manages_ok_button(owner_cards)
        elif card_button['bg'] == 'gray':
            card_button['bg'] = 'SystemButtonFace'
            CardsAndHands().selected_card(owner_cards, '', del_card = card_button['text'])
            self.manages_ok_button(owner_cards)

    def ok_button_click(self, top_level: object, caller_button: object, entry: object, owner_cards: str):
        if owner_cards == 'Flop':
            text = f'{selected_cards[owner_cards][0]}{selected_cards[owner_cards][1]}{selected_cards[owner_cards][2]}'
        elif owner_cards == 'Turn' or owner_cards == 'River':
            text = f'{selected_cards[owner_cards][0]}'
        else:
            text = f'{selected_cards[owner_cards][0]}{selected_cards[owner_cards][1]}'

        self.entry.delete(0, 'end')
        self.entry.insert(0, text)

        top_level.destroy()
        caller_button['state'] = 'active'

    def cancel_button_click(self, top_level: object, caller_button: object, entry: object, owner_cards: str):
        # delete the cards from the list
        selected_cards[owner_cards] = []

        top_level.destroy()
        caller_button['state'] = 'active'

