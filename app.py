import tkinter, itertools
from pprint import pprint
from tkinter import ttk


class PokerRangeAnalysis:
    ''' creates the main application '''

    def __init__(self, master:object) -> object:
        self.master = master
        self.master.title('Poker Range Analysis')

        self.creates_global_variables_lists_dicts()
        self.creates_tab_control(master)
        self.creates_tabs_layouts(master, self.tab_control)
        self.creates_poker_cards()
        self.creates_poker_cards_combinations()
        
        return None

    def creates_global_variables_lists_dicts(self) -> dict:
        '''method used only to store global variables'''
        global figures_list, naipes_list, cards_matrix, cards_and_hands_dict, selected_cards, \
            range_dict, select_hands_total_combo, total_combinations, streets_labels_dict, current_color_button_name

        figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        naipes_list = [('d','#014082'), ('h','#CC0000'), ('s','#000000'), ('c','#00732B')]
        cards_matrix = [[figure + naipe[0] for figure in figures_list] for naipe in naipes_list]

        cards_and_hands_dict = {
            'hands': [], 
            'combinations': {},
            'removed_combinations': {},
            'card_buttons': {},
            }
        
        selected_cards = {'Hero':[], 'Flop':[], 'Turn':[], 'River':[]}


        range_dict = {'Pré-Flop':{}, 'Flop':{}, 'Turn':{}, 'River':{}}

        select_hands_total_combo = 0
        total_combinations = 0

        streets_labels_dict = {}

        current_color_button_name = ''

        return cards_and_hands_dict

    def creates_tab_control(self, master:object) -> object:
        self.tab_control = ttk.Notebook(master)
        self.tab_control.grid(padx = 5, pady = 5)

    def creates_tabs_layouts(self, master:object, tab_control:object) -> object:
        # Tab Start
        tab_start = ttk.Frame(tab_control, width = 546, height = 210)
        tab_control.add(tab_start, text="Início")

        # Frame Basic Informations
        label_frame = tkinter.LabelFrame(tab_start, text = "Informações Básicas", width = 258, height = 78, padx = 10, pady = 5)
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

        # Frame Opponent Informations
        label_frame = tkinter.LabelFrame(tab_start, text = "Informações do Vilão", width = 258, height = 78, padx = 10, pady = 5)
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

        # Frame Notes And Infos
        label_frame = tkinter.LabelFrame(tab_start, text = "Notes e Infos", width = 258, height = 100, padx = 5, pady = 10)
        label_frame.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2, sticky = 'we')

        label_notes = tkinter.Label(label_frame, text = 'Notes')
        label_notes.grid(row = 0, column = 0, sticky = 'w')

        textbox_notes = tkinter.Text(label_frame, width = 35, height = 3)
        textbox_notes.grid(row = 1, column = 0, padx = 5)

        label_infos = tkinter.Label(label_frame, text = 'Infos')
        label_infos.grid(row = 0, column = 1, sticky = 'w')

        textbox_infos = tkinter.Text(label_frame, width = 35, height = 3)
        textbox_infos.grid(row = 1, column = 1, padx = 5)

        tabs_streets = {
            'Pré-Flop': {'tab_name': 'PF', 'qtd': 2}, 'Flop': {'tab_name': 'F', 'qtd': 3}, 
            'Turn': {'tab_name': 'T', 'qtd': 3}, 'River': {'tab_name': 'R', 'qtd': 3}
            }

        # Others tabs
        for street in tabs_streets:
            main_frame = tkinter.Frame()
            path = tabs_streets[street]

            self.creates_frame_streets_buttons(main_frame, street, path['qtd'], path['tab_name'], 0, 0)
            self.creates_frame_streets_equity(main_frame, path['tab_name'], path['qtd'], 'equity', 0, 1)
            self.creates_frame_streets_equity(main_frame, path['tab_name'], path['qtd'], 'fold_equity', 0, 2)
            self.creates_frame_streets_select_cards(master, 1, 0)
            self.tab_control.add(main_frame, text = street)

    def creates_frame_streets_buttons(self, master:object, street:str, qtd:str, btn_name:str, row:str, column:str) -> object:
        self.street = street
        self.qtd = qtd
        self.btn_name = btn_name
        self.row = row
        self.column = column

        global range_dict

        frame_buttons = tkinter.Frame(master)
        frame_buttons.grid(row = self.row, column = self.column, sticky = 's', ipady = 7)
    
        for n in range(self.qtd):
            button_name = f'{self.btn_name}{n + 1}'
            button = tkinter.Button(frame_buttons, text = button_name, width = 10)
            button.config(command = lambda button = button, street = street: WindowRangeSelection(button, street))
            button.grid(row = n, column = 0, padx = 5, pady = 5, sticky = 's')

            range_dict[street][button_name] = {
                'caller_button': button, 
                'range_detail': {
                    'RF+': {'color': '#B2301E'}, 'RFF': {'color' : '#BE6EAE'}, 'RF-': {'color': '#EA8376'}, 
                    'RM+': {'color': '#4572A9'}, 'RM-': {'color': '#81ACDF'}, 'RF': {'color': '#E8950F'},
                    'RF-': {'color': '#FFCD69'}, 'SPLIT': {'color': '#27A2A1'}
                }
            }
        return range_dict[street]

    def creates_frame_streets_equity(self, master:object, street:str, rows:str, table_type:str, row:str, column:str) -> object:
        self.street = street
        self.rows = rows
        self.table_type = table_type
        self.row = row
        self.column = column
        
        global streets_labels_dict

        title_dict = {
            'equity': ['Range\n(mãos)', 'Eq. Vilão\n(%)', 'Eq. Hero\n(%)', 'Split\n(%)'],
            'fold_equity': ['FE/Block\n(mãos)', 'FE/Block\n(%)', 'Cbet\n(%)'],
        }
        
        # main frame
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10)

        # create the labels with the titles
        for i in range(len(title_dict[self.table_type])):
            label = tkinter.Label(range_frame, text = title_dict[self.table_type][i])
            label.grid(row = 0, column = i, padx = 5)

        # create the entries(?)
        for i in range(len(title_dict[self.table_type])):
            foo = str(f'{title_dict[self.table_type][i]}').replace('\n', '_').replace('. ', '_').replace('_(%)', '')
            for x in range(self.rows):
                label = tkinter.Label(range_frame, width = 8, relief = 'groove', bg = 'white')
                label.grid(row = x + 1, column = i, padx = 5, pady = 7)
                streets_labels_dict[f'{street}{x+1}_{foo}'] = label

    def creates_frame_streets_select_cards(self, master: object, row:str, column:str) -> object:
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
            button_choose.config(command = lambda label_name = label_name, button_choose = button_choose, 
            entry = entry: WindowCardSelection(label_name, button_choose, entry).create_gui(label_name))
            
            button_clear = tkinter.Button(frame, image = img_clear, command = lambda entry = entry, 
            button_choose = button_choose, label_name = label_name: self.clear_button_click(entry, button_choose, label_name))
            button_clear.image = img_clear  # keep a reference
            button_clear.grid(row = 0, column = 3)

    def clear_button_click(self, entry:object, button_choose:object, label_name:str):
        WindowCardSelection(label_name, button_choose, entry).manages_cards(label_name, add_card = '', del_card = entry.get())
        entry.delete(0, 'end')
        button_choose['state'] = 'active'

    def creates_poker_cards(self) -> list:
        global cards_and_hands_dict, figures_list

        # creates a list with all hands
        for f1 in figures_list:
            for f2 in figures_list:
                if f1 == f2:
                    if f1+f2 not in cards_and_hands_dict['hands']:
                        cards_and_hands_dict['hands'].append(f1+f2)
                elif figures_list.index(f1) < figures_list.index(f2):
                    if f1+f2+'s' not in cards_and_hands_dict['hands']:
                        cards_and_hands_dict['hands'].append(f1+f2+'s')
                elif f1+f2+'o' not in cards_and_hands_dict['hands']:
                        cards_and_hands_dict['hands'].append(f2+f1+'o')

        return cards_and_hands_dict['hands']

    def creates_poker_cards_combinations(self) -> dict:
        # separate hands into pairs, suiteds and off-suiteds to make the combinations
        
        pairs = []
        suiteds = []
        off_suiteds = []

        for hand in cards_and_hands_dict['hands']:
            if hand[0] == hand[1]:
                pairs.append(hand)
            elif 's' in hand:
                suiteds.append(hand)
            elif 'o' in hand:
                off_suiteds.append(hand)

        naipes = "dhsc"
        for hand in pairs:
            cards_and_hands_dict['combinations'][hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
            for naipe in itertools.combinations(naipes, len(hand))]

        for hand in suiteds:
            cards_and_hands_dict['combinations'][hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
            for naipe in list(itertools.product(naipes, repeat=2))]

        # gambiarra pra deixar somente as mãos suited
        for hand in suiteds:
            for combo in cards_and_hands_dict['combinations'][hand][:]:
                if combo[0][1] != combo[1][1]:
                    cards_and_hands_dict['combinations'][hand].remove(combo)

        for hand in off_suiteds:
            cards_and_hands_dict['combinations'][hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
            for naipe in list(itertools.product(naipes, repeat=2))]

        # gambiarra pra deixar somente as mãos 0ff-suiteds
        for hand in off_suiteds:
            for combo in cards_and_hands_dict['combinations'][hand][:]:
                if combo[0][1] == combo[1][1]:
                    cards_and_hands_dict['combinations'][hand].remove(combo)
        return cards_and_hands_dict['combinations']


class WindowCardSelection:
    '''Creates a window for selecting Hero, Flop, Turn and River cards'''

    def __init__(self, owner_cards:str, caller_button:object, entry:object) -> object:
        self.owner_cards = owner_cards
        self.caller_button = caller_button
        self.caller_button['state'] = 'disabled'
        self.entry = entry

    def create_gui(self, owner_cards:str) -> object:
        '''Creates the window interface'''

        global cards_and_hands_dict  

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
        
        for row in range(4):
            for col in range(13):
                card_button_name = cards_matrix[row][col]
                card_button_color = naipes_list[row][1]

                card_button = tkinter.Button(cards_frame, width = 2, heigh = 2, text = card_button_name, fg = card_button_color, relief = 'groove')
                card_button.grid(row = row, column = col, padx = 1, pady = 1)
                card_button.config(command = lambda card_button = card_button: self.card_button_click(owner_cards, card_button))

                cards_and_hands_dict['card_buttons'][card_button_name] = card_button
                
        # creates auxiliary buttons
        self.ok_button = tkinter.Button(main_frame, text = 'OK', width = 6, state = 'disabled')
        self.ok_button.config(command = lambda: self.ok_button_click(window_card_selection, self.caller_button, self.entry, self.owner_cards))
        self.ok_button.grid(row = 1, column = 0, pady = 5)

        self.cancel_button = tkinter.Button(main_frame, text = 'Cancel', width = 6, command = lambda: self.cancel_button_click(window_card_selection, self.caller_button, self.entry, self.owner_cards))
        self.cancel_button.grid(row = 1, column = 1, pady = 5)

        self.check_entry_filled(self.owner_cards, self.entry)

        return cards_and_hands_dict['card_buttons']

    def check_entry_filled(self, owner_cards:str, entry:object):
        '''Identifies whether you already have cards in the entry (added manually or previously selected)'''

        global selected_cards, cards_and_hands_dict

        # extracts the list of cards from the current owner
        list_selected_cards = self.manages_cards(owner_cards, entry.get()) 
        if list_selected_cards:
            selected_cards[owner_cards] = []  # clears the list of cards and resends the command to select
            for card in list_selected_cards:
                self.card_button_click(owner_cards, cards_and_hands_dict['card_buttons'][card])

        # Identifies the cards already selected on the other streets and disables them
        for key in selected_cards:
            if key != owner_cards:
                for card in selected_cards[key]:
                    cards_and_hands_dict['card_buttons'][card]['state'] = 'disabled'

        return list_selected_cards

    def card_button_click(self, owner_cards:str, card_button:object):
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

        if permission == True and card_button['bg'] == 'SystemButtonFace':
            card_button['bg'] = 'gray'
            self.manages_cards(owner_cards, add_card = card_button['text'])
            self.manages_ok_button(owner_cards)
        elif card_button['bg'] == 'gray':
            card_button['bg'] = 'SystemButtonFace'
            self.manages_cards(owner_cards, '', del_card = card_button['text'])
            self.manages_ok_button(owner_cards)

    def manages_cards(self, owner_cards:str, add_card:str, del_card:str ='') -> list:
        '''receives the text of the entry or the card buttons and inserts the cards in the list of their respective "owner" '''
        
        global selected_cards

        # extracts the two cards from the text
        add_card_1 = add_card[0:2].capitalize()
        add_card_2 = add_card[2:4].capitalize()
        add_card_3 = add_card[4:6].capitalize()
        del_card_1 = del_card[0:2].capitalize()
        del_card_2 = del_card[2:4].capitalize()
        del_card_3 = del_card[4:6].capitalize()

        # insert the cards in the list
        if add_card_1 and add_card_1 not in selected_cards[owner_cards]:
            selected_cards[owner_cards].append(add_card_1)
            self.removes_combos(add_card_1)
        if add_card_2 and add_card_2 not in selected_cards[owner_cards]:
            selected_cards[owner_cards].append(add_card_2)
            self.removes_combos(add_card_2)
        if add_card_3 and add_card_3 not in selected_cards[owner_cards]:
            selected_cards[owner_cards].append(add_card_3)
            self.removes_combos(add_card_3)

        # delete the cards from the list
        if del_card_1:
            selected_cards[owner_cards].remove(del_card_1)
            self.re_add_combos(del_card_1, owner_cards)
        if del_card_2:
            selected_cards[owner_cards].remove(del_card_2)
            self.re_add_combos(del_card_2, owner_cards)
            self.re_add_combos(del_card_1, owner_cards)
        if del_card_3:
            selected_cards[owner_cards].remove(del_card_3)
            self.re_add_combos(del_card_3, owner_cards)

        return selected_cards[owner_cards]

    def removes_combos(self, card:str) -> dict:
        '''removes all combinations of hands using this card'''
        global cards_and_hands_dict

        # create a dictionary with the combinations that will be deleted
        for hand in cards_and_hands_dict['combinations']:
            for combo in cards_and_hands_dict['combinations'][hand]:
                if card in combo[0] or card in combo[1]:
                    if hand not in cards_and_hands_dict['removed_combinations']:
                        cards_and_hands_dict['removed_combinations'][hand] = []
                        cards_and_hands_dict['removed_combinations'][hand].append(combo)
                    elif hand in cards_and_hands_dict['removed_combinations'] and combo not in cards_and_hands_dict['removed_combinations'][hand]:
                        cards_and_hands_dict['removed_combinations'][hand].append(combo)

        # deletes combinations from the original dictionary
        for hand in cards_and_hands_dict['removed_combinations']:
            for combo in cards_and_hands_dict['removed_combinations'][hand]:
                if combo in cards_and_hands_dict['combinations'][hand]:
                    cards_and_hands_dict['combinations'][hand].remove(combo)

        return cards_and_hands_dict['removed_combinations'], cards_and_hands_dict['combinations']

    def re_add_combos(self, card:str, owner_cards:str) -> dict:
        ''' when you deselect a card, all combos of that card are returned to the main dictionary'''
        
        global selected_cards, cards_and_hands_dict
        
        locked_cards = []
        for owner_cards in selected_cards:
            for card in selected_cards[owner_cards]:
                locked_cards.append(card)

        # based on the auxiliary dictionary, re-add combos from the main dictionary
        for hand in cards_and_hands_dict['removed_combinations']:
            for combo in cards_and_hands_dict['removed_combinations'][hand]:
                if (card in combo[0] and combo[1] not in locked_cards) or (card in combo[1] and combo[0] not in locked_cards):
                        cards_and_hands_dict['combinations'][hand].append(combo)
        
        # after re-add in main dictionary, it also removes combos from the auxiliary dictionary
        for hand in cards_and_hands_dict['removed_combinations']:
            for combo in list(cards_and_hands_dict['removed_combinations'][hand]): # way to remove items from a dictionary by iterating over it
                if (card in combo[0] and combo[1] not in locked_cards) or (card in combo[1] and combo[0] not in locked_cards):
                    cards_and_hands_dict['removed_combinations'][hand].remove(combo)

        return cards_and_hands_dict['removed_combinations']

    def manages_ok_button(self, owner_cards:str) -> bool:
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

    def ok_button_click(self, top_level:object, caller_button:object, entry:object, owner_cards:str):
        ''' Insert the selected cards into the entry and close the window '''

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

    def cancel_button_click(self, top_level:object, caller_button:object, entry:object, owner_cards:str):
        ''' delete the cards from the list '''

        selected_cards[owner_cards] = []
        entry.delete(0, 'end')
        
        top_level.destroy()
        caller_button['state'] = 'active'


class WindowRangeSelection:
    '''Creates a window for selecting Pré-Flop, Flop, Turn and River ranges'''

    def __init__(self, caller_button:object, street:str) -> object:
        global select_hands_total_combo, total_combinations
        select_hands_total_combo = 0
        total_combinations = 0

        self.caller_button = caller_button
        self.street = street
        self.caller_button['state'] = 'disabled'

        self.range_window = tkinter.Toplevel()
        self.range_window.title(f"Selecione o Range - {caller_button['text']}")
        self.range_window.wm_resizable('false', 'false')
        self.range_window.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_click(self.range_window, self.caller_button, self.street))

        self.create_hand_buttons_matrix(self.range_window, 0, 0, caller_button)
        self.creates_auxiliary_buttons(self.range_window, 0, 1, self.caller_button['text'], self.street)
        self.creates_space_comments(self.range_window, 2, 0)
        self.creates_ok_and_cancel_buttons(self.range_window, 3, 0)
        self.check_range_pre_selected(self.caller_button, self.street)

    def create_hand_buttons_matrix(self, master: object, row:str, column:str, street_name:str):
        self.row = row
        self.column = column
        self.street_name = street_name
        self.range_buttons = [[None for x in range(13)] for x in range (13)]

        global select_hands_total_combo, total_combinations

        cards_frame = tkinter.Frame(master)
        cards_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10)

        hands_index = 0
        self.hand_buttons_dict = {}

        for row in range (13):
            for col in range (13):
                hand_button_pre_name = cards_and_hands_dict['hands'][hands_index]
                hand_button_n_combos = len(cards_and_hands_dict['combinations'][hand_button_pre_name])
                hand_button_name = f'{hand_button_pre_name}\n{hand_button_n_combos}'
                original_color = '#FFE7B5' if 's' in hand_button_name else '#E7EFF7' if 'o' in hand_button_name else '#CFDFC7'

                hand_button = self.range_buttons[row][col] = tkinter.Button(cards_frame, width = 5, bg = original_color, text = hand_button_name)
                hand_button.grid(row = row, column = col)

                if hand_button_n_combos == 0:
                    hand_button['state'] = 'disabled'
                hand_button.config(command = lambda hand_button = hand_button, hand_button_pre_name = hand_button_pre_name, original_color = original_color: self.select_hand(hand_button, hand_button_pre_name, original_color, street_name['text'], self.street))

                self.hand_buttons_dict[hand_button_pre_name] = (hand_button, original_color)
                hands_index += 1
                total_combinations += hand_button_n_combos
        
    def creates_auxiliary_buttons(self, master: object, row: str, column:str, caller_button: str, street:str):
        """Creates auxiliary color buttons, clear and next slot"""

        self.row = row
        self.column = column
        self.caller_button = caller_button
        self.street = street

        global range_dict

        frame_auxiliary = tkinter.Frame(master)
        frame_auxiliary.grid(row = self.row, column = self.column, padx = 5)

        button_clear = tkinter.Button(frame_auxiliary, text = 'Limpar', command = lambda: self.clear_hands(self.caller_button, self.street))
        button_clear.grid(padx = 5, pady = 20)
        
        for key, value in range_dict[street][caller_button]['range_detail'].items():
            color_button = tkinter.Button(frame_auxiliary, width = 4, text = key, bg =  value['color'])
            color_button.grid(pady = 5)
            color_button.config(command = lambda key = key: self.pick_color(key, self.street, self.caller_button))

            range_color_label = tkinter.Label(frame_auxiliary, text = 0)
            range_color_label.grid()

            value['button'] = color_button
            value['label'] = range_color_label

        next_slot_button = tkinter.Button(frame_auxiliary, text = 'Próximo Slot', command = lambda caller_button = caller_button, street = street: self.next_slot_click(self.range_window, caller_button, street))
        next_slot_button.grid(pady = 30)

        if caller_button == 'R3':
            next_slot_button['state'] = 'disabled'

        return range_dict[street]

    def creates_space_comments(self, master: object, row:str, column:str):
        self.row = row
        self.column = column

        global select_hands_total_combo, total_combinations

        frame_comments = tkinter.Frame(master)  
        frame_comments.grid(row = self.row, column = self.column, padx = 5, pady = 5)

        self.label_combo_count = tkinter.Label(frame_comments, text = f'Leque de mãos selecionado contém {select_hands_total_combo}/{total_combinations} mãos (0.00%)')
        self.label_combo_count.grid(row = 0, column = 0, pady = 5)
        label_comments = tkinter.Label(frame_comments, text = 'Comentários')
        label_comments.grid(row = 1, column = 0, sticky = 'w')
        text_box = tkinter.Text(frame_comments, width = 72, height = 1)
        text_box.grid(row = 2, column = 0, padx = 5, pady = 5)

    def creates_ok_and_cancel_buttons(self, master:object, row:str, column:str):
        self.row = row
        self.column = column

        frame_buttons = tkinter.Frame(master)
        frame_buttons.grid(row = self.row, column = self.column, padx = 5, pady = 5)

        ok_button = tkinter.Button(frame_buttons, text = 'OK', width = 6, command = lambda: self.ok_button_click(self.range_window, self.caller_button, self.street))
        ok_button.grid(row = 0, column = 0, padx = 5, pady = 5)

        cancel_button = tkinter.Button(frame_buttons, text = 'Cancel', width = 6, command = lambda: self.cancel_button_click(self.range_window, self.caller_button, self.street))
        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5)

    def check_range_pre_selected(self, caller_button:object, street:str):
        global range_dict, select_hands_total_combo

        path = range_dict[street][caller_button]['range_detail']
        for key, value in path.items():
            if 'selected_range' in path[key] and path[key]['selected_range']:
                if path[key]['button']['relief'] == 'raised':
                    self.pick_color(key, street, caller_button)
                for hand in value['selected_range'][:]:
                    self.select_hand(self.hand_buttons_dict[hand][0], hand, self.hand_buttons_dict[hand][1], caller_button, street)

    def ok_button_click(self, top_level:object, caller_button:str, street:str):
        global select_hands_total_combo, streets_labels_dict, range_dict
        
        if select_hands_total_combo > 0:
            streets_labels_dict[f'{caller_button}_Range_(mãos)']['text'] = select_hands_total_combo
            
            # calcula  a equidade do vilão
            path = range_dict[street][caller_button]['range_detail']
            split = 0
            range_fraco = 0
            range_medio = 0
            range_forte = 0
            for key in path:
                # split
                if key == 'SPLIT':
                    split = path[key]['label']['text']

                # range medio
                if key in ['RM+', 'RM-']:
                    range_medio += path[key]['label']['text']
                
                #range fraco
                if key == 'RF':
                    range_fraco = path[key]['label']['text']

                # range forte
                if key in ['RF+', 'RFF', 'RF-']:
                    range_forte += path[key]['label']['text']

                streets_labels_dict[f'{caller_button}_Split']['text'] = f'{(split / select_hands_total_combo) * 100:.2f}%'
                streets_labels_dict[f'{caller_button}_Eq_Hero']['text'] = f'{((range_fraco + range_medio / 2 )/ select_hands_total_combo) * 100:.2f}%'
                streets_labels_dict[f'{caller_button}_Eq_Vilão']['text'] = f'{((range_forte + range_medio / 2) / select_hands_total_combo) * 100:.2f}%'
        else: 
                streets_labels_dict[f'{caller_button}_Range_(mãos)']['text'] = ''
                streets_labels_dict[f'{caller_button}_Split']['text'] = ''
                streets_labels_dict[f'{caller_button}_Eq_Hero']['text'] = ''
                streets_labels_dict[f'{caller_button}_Eq_Vilão']['text'] = ''

        top_level.destroy()
        range_dict[street][caller_button]['caller_button']['state'] = 'active'

    def cancel_button_click(self, top_level:object, caller_button:str, street:str):
        global range_dict
        
        top_level.destroy()
        range_dict[street][caller_button]['caller_button']['state'] = 'active'

    def select_hand(self, hand_button:object, hand_button_name:str, original_color:str, caller_button:str, street:str):
        """if any color button is selected, when clicking on the card button, its color is changed"""

        global current_color_button_name, select_hands_total_combo, range_dict, cards_and_hands_dict, total_combinations

        if current_color_button_name: # apenas se alguma cor estiver selecionada
            path = range_dict[street][caller_button]['range_detail'][current_color_button_name]

        if current_color_button_name and hand_button['bg'] == original_color:
            hand_button['bg'] = path['color']

            select_hands_total_combo += len(cards_and_hands_dict['combinations'][hand_button_name])
            percentual = (select_hands_total_combo / total_combinations) * 100
            self.label_combo_count['text'] = f'Leque de mãos selecionado contém {select_hands_total_combo}/{total_combinations} mãos ({percentual:.2f}%)'
            
            path['label']['text'] += len(cards_and_hands_dict['combinations'][hand_button_name])

            # adiciona a mão selecionada no range da street específica e da cor específica
            if 'selected_range' not in path:
                path['selected_range'] = []

                if hand_button_name not in path['selected_range']:
                    path['selected_range'].append(hand_button_name)

            elif hand_button_name not in path['selected_range']:
                path['selected_range'].append(hand_button_name)

            # if 'combo_color_range' not in path:
            #     # range_dict[caller_button]['range_detail'][current_color_button_name]['combo_color_range'] = 0
            #     path['combo_color_range'] = path['label']['text']
            #     # print(caller_button, current_color_button_name, range_dict['PF1']['range_detail']['RF+'])
            # else:
            #     path['combo_color_range'] = path['label']['text']

        elif current_color_button_name and hand_button['bg'] == path['button']['bg']:
            hand_button.config(bg = original_color)

            select_hands_total_combo -= len(cards_and_hands_dict['combinations'][hand_button_name])
            percentual = (select_hands_total_combo / total_combinations) * 100
            self.label_combo_count['text'] = f'Leque de mãos selecionado contém {select_hands_total_combo}/{total_combinations} mãos ({percentual:.2f}%)'
            
            path['label']['text'] -= len(cards_and_hands_dict['combinations'][hand_button_name])
            path['selected_range'].remove(hand_button_name)

        elif current_color_button_name and hand_button['bg']: #já estava selecionado com outra cor 
            # identifica a cor anterior
            old_path = range_dict[street][caller_button]['range_detail']
            for color_button in old_path:
                if hand_button['bg'] == old_path[color_button]['color']:
                    old_color = color_button

            # altera para a cor atual e atualiza os dicionários
            hand_button['bg'] = range_dict[street][caller_button]['range_detail'][current_color_button_name]['color']

            old_path[old_color]['label']['text'] -= len(cards_and_hands_dict['combinations'][hand_button_name])
            old_path[old_color]['selected_range'].remove(hand_button_name)

            new_path = range_dict[street][caller_button]['range_detail'][current_color_button_name]
            new_path['label']['text'] += len(cards_and_hands_dict['combinations'][hand_button_name])

            if 'selected_range' not in new_path:
                new_path['selected_range'] = []

                if hand_button_name not in new_path['selected_range']:
                    new_path['selected_range'].append(hand_button_name)

            elif hand_button_name not in new_path['selected_range']:
                new_path['selected_range'].append(hand_button_name)

    def pick_color(self, color_button_name:object, street:str, caller_button:str):
        global current_color_button_name, range_dict

        path = range_dict[street][caller_button]['range_detail']

        # disabel other buttons
        for key in path:
            if key != color_button_name:
                path[key]['button']['relief'] = 'raised'

        # pick a color
        if path[color_button_name]['button']['relief'] == 'raised':
            path[color_button_name]['button']['relief'] = 'sunken'
            current_color_button_name = color_button_name
        elif path[color_button_name]['button']['relief'] == 'sunken':
            path[color_button_name]['button']['relief'] = 'raised'
            current_color_button_name = ''

    def clear_hands(self, caller_button:str, street:str):
        global current_color_button_name, select_hands_total_combo, range_dict

        # automaticamente deseleciona todas as cartas
        self.check_range_pre_selected(caller_button, street)

        # esquema para deselecionar os botoes de cor e limpar o current color
        path = range_dict[street][caller_button]['range_detail']

        for color_button_name in path:
            path[color_button_name]['button']['relief'] = 'raised'
        current_color_button_name = ''

    def next_slot_click(self, top_level:object, caller_button:object, street:str):
        global range_dict

        self.ok_button_click(top_level, caller_button, street)

        # encontra a proxima street e o proximo botao de range
        streets_buttons_list = {}
        for s in range_dict:
            streets_buttons_list[s] = list(range_dict[s])

        for s in streets_buttons_list:
            if caller_button in streets_buttons_list[s]:
                try:
                    next_button_name = streets_buttons_list[s][streets_buttons_list[s].index(caller_button) + 1]
                    next_street = s
                    next_button = range_dict[next_street][next_button_name]['caller_button']
                except IndexError:
                    next_street = list(streets_buttons_list)[list(streets_buttons_list).index(s) + 1]
                    next_button_name = streets_buttons_list[next_street][0]
                    next_button = range_dict[next_street][next_button_name]['caller_button']
        

        # copia os ranges da street atual para a proxima street
        old_path = range_dict[street][caller_button]['range_detail']
        new_path = range_dict[next_street][next_button_name]['range_detail']

        for key in old_path:
            if 'selected_range' in old_path[key]:
                new_path[key]['selected_range'] = old_path[key]['selected_range']
        
        # abre a janela da proxima street
        WindowRangeSelection(next_button, next_street)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.wm_resizable(False, False)
    x = PokerRangeAnalysis(root)
    root.mainloop()
