import tkinter


current_color = ''
selected_cards = {'Hero':[], 'Flop':[], 'Turn':[], 'River':[]}

class FrameStreetsButtons:
    def __init__(self, master, qtd, name, row, column):
        self.qtd = qtd
        self.name = name
        self.row = row
        self.column = column

        frame_buttons = tkinter.Frame(master)
        frame_buttons.grid(row = self.row, column = self.column, sticky = 's', ipady = 8)
    
        for n in range(self.qtd):
            button = tkinter.Button(frame_buttons, text = f'{self.name}{n + 1}', 
                width = 10, command = WindowRangeSelection)
            button.grid(row = n, column = 0, padx = 5, pady = 3, sticky = 's')

class FrameStreetsEquity:
    def __init__(self, master, rows, table_type, row, column):
        self.rows = rows
        self.table_type = table_type
        self.row = row
        self.column = column

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
            for x in range(self.rows):
                entry = tkinter.Entry(range_frame, width = 8)
                entry.grid(row = x + 1, column = i, padx = 5, pady = 7)

class FrameStreetsSelectCards:
    def __init__(self, master, row, column):
        self.row = row
        self.column = column

        # main frame
        main_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        main_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10, columnspan = 3)

        labels_list = ['Hero', 'Flop', 'Turn', 'River']
        img_cards = tkinter.PhotoImage(file = 'interface/images/card_selection.png')
        img_clear = tkinter.PhotoImage(file = 'interface/images/button_clear.png')

        for i in range(len(labels_list)):
            label_name = labels_list[i]

            frame = tkinter.Frame(main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{label_name}:')
            label.grid(row = 0, column = 0)

            entry = tkinter.Entry(frame, width = 5)
            entry.grid(row = 0, column = 1, padx = 5)

            button_choose = tkinter.Button(frame, image = img_cards)
            button_choose.image = img_cards  # Keep a reference
            button_choose.grid(row = 0, column = 2, padx = 5, pady = 5)
            button_choose.config(command = lambda label_name = label_name, button_choose = button_choose, entry = entry: WindowCardSelection(label_name, button_choose, entry))
            button_clear = tkinter.Button(frame, image = img_clear, command = lambda entry = entry, button_choose = button_choose, label_name = label_name: self.clear_button_click(entry, button_choose, label_name))
            button_clear.image = img_clear  # keep a reference
            button_clear.grid(row = 0, column = 3)

    def clear_button_click(self, entry: object, button_choose: object, label_name:str):
        entry.delete(0, 'end')
        button_choose['state'] = 'active'
        selected_cards[label_name] = []

class WindowRangeSelection:
    def __init__(self):
        self.range_window = tkinter.Toplevel()
        self.range_window.title("Selecione o Range")
        self.create_card_buttons_matrix(self.range_window, 0, 0)
        self.creates_auxiliary_buttons(self.range_window, 0, 1)
        self.creates_space_comments(self.range_window, 2, 0)

    def create_card_buttons_matrix(self, master, row, column):
        self.row = row
        self.column = column
        self.range_buttons = [[None for x in range(13)] for x in range (13)]

        cards_frame = tkinter.Frame(master)
        cards_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10)
        hands = ['AA', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s', 
                      'AKo', 'KK', 'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
                      'AQo', 'KQo', 'QQ', 'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s',
                      'AJo', 'KJo', 'QJo', 'JJ', 'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s',
                      'ATo', 'KTo', 'QTo', 'JTo', 'TT', 'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s',
                      'A9o', 'K9o', 'Q9o', 'J9o', 'T9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s',
                      'A8o', 'K8o', 'Q8o', 'J8o', 'T8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s',
                      'A7o', 'K7o', 'Q7o', 'J7o', 'T7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s',
                      'A6o', 'K6o', 'Q6o', 'J6o', 'T6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s',
                      'A5o', 'K5o', 'Q5o', 'J5o', 'T5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s',
                      'A4o', 'K4o', 'Q4o', 'J4o', 'T4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s',
                      'A3o', 'K3o', 'Q3o', 'J3o', 'T3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s',
                      'A2o', 'K2o', 'Q2o', 'J2o', 'T2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22', 
        ]
        self.card_buttons_dict = {}
        hands_index = 0
        for row in range (13):
            for col in range (13):
                text = hands[hands_index]
                color = '#FFE7B5' if 's' in text else '#E7EFF7' if 'o' in text else '#CFDFC7'
                hand_button = self.range_buttons[row][col] = tkinter.Button(
                    cards_frame, width = 3, bg = color, text = text)
                hand_button.grid(row = row, column = col)
                hand_button.config(command = lambda hand_button = hand_button, 
                    color = color: self.select_hand(hand_button, color))
                self.card_buttons_dict[text] = (hand_button, color)
                hands_index += 1
        
    def creates_auxiliary_buttons(self, master, row, column):
        self.row = row
        self.column = column
        self.color_buttons_dict = {}
        colors_dict = {'RF+': '#B2301E', 'RFF': '#BE6EAE', 'RF-': '#EA8376', 
                       'RM+': '#4572A9', 'RM-': '#81ACDF', 'RF': '#E8950F',
                       'RF-': '#FFCD69', 'SPLIT': '#27A2A1'}

        frame_auxiliary = tkinter.Frame(master)
        frame_auxiliary.grid(row = self.row, column = self.column, padx = 5)
        button_clear = tkinter.Button(frame_auxiliary, text = 'Limpar',
            command = lambda: self.clear_cards())
        button_clear.grid(padx = 5, pady = 10)
        for key, color in colors_dict.items():
            color_button = tkinter.Button(frame_auxiliary, width = 4, 
                text = key, bg = color)
            color_button.grid(pady = 5)
            color_button.config(command = lambda color_button = color_button, 
                color = color: self.pick_color(color_button, color))
            self.color_buttons_dict[key] = color_button

    def creates_space_comments(self, master, row, column):
        self.row = row
        self.column = column

        frame_comments = tkinter.Frame(master)
        frame_comments.grid(row = self.row, column = self.column, padx = 5, pady = 5)
        label_comments = tkinter.Label(frame_comments, text = 'Comentários')
        label_comments.grid(row = 0, column = 0)
        text_box = tkinter.Text(frame_comments, width = 50, height = 5)
        text_box.grid(row = 1, column = 0, padx = 5, pady = 5)

    def select_hand(self, card_button, color):
        global current_color
        if current_color:
            card_button.config(bg = current_color)
        else:
            card_button.config(bg = color)

    def pick_color(self, color_button, color):
        global current_color
        # disabel other buttons
        for button in self.color_buttons_dict.values():
            if button != color_button:
                button['relief'] = 'raised'

        if color_button['relief'] == 'raised':
            color_button['relief'] = 'sunken'
            current_color = color
        elif color_button['relief'] == 'sunken':
            color_button['relief'] = 'raised'
            current_color = ''

    def clear_cards(self):
        for card_button in self.card_buttons_dict.values():
            card_button[0]['bg'] = card_button[1]
        for color_button in self.color_buttons_dict.values():
            color_button['relief'] = 'raised'

class WindowCardSelection:
    def __init__(self, owner_cards:str, caller_button:object, entry:object) -> object:
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
                card_button_name = CardsAndHands().generate_cards(row, col)
                card_button_color = CardsAndHands().naipes_list[row][1]

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
        if len(selected_cards[owner_cards]) == 2:
            self.ok_button['state'] = 'active'
            return False
        else:
            self.ok_button['state'] = 'disabled'
            return True

    def card_button_click(self, owner_cards:str, card_button_name:str):
        '''Select and deselect cards if possible'''

        # checks the number of cards that have already been selected
        if len(selected_cards[owner_cards]) == 2:
            permission = False
        else:
            permission = True
        
        # identifies the object (button) by name
        card_button = self.card_button_dict[card_button_name]

        if permission == True and card_button['bg'] == 'SystemButtonFace':
            print('carta selecionada')
            card_button['bg'] = 'gray'
            CardsAndHands().selected_card(owner_cards, add_card = card_button['text'])
            self.manages_ok_button(owner_cards)
        elif card_button['bg'] == 'gray':
            card_button['bg'] = 'SystemButtonFace'
            CardsAndHands().selected_card(owner_cards, '', del_card = card_button['text'])
            self.manages_ok_button(owner_cards)

    def ok_button_click(self, top_level: object, caller_button: object, entry: object, owner_cards: str):
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

class CardsAndHands:
    def __init__(self):
        self.figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        self.naipes_list = [('d','#014082'), ('h','#CC0000'), ('s','#000000'), ('c','#00732B')]
    
    def generate_cards(self, index1, index2):
        cards = [[figure + naipe[0] for figure in self.figures_list] for naipe in self.naipes_list]
        return cards[index1][index2]

    def selected_card(self, owner_cards:str, add_card:str, del_card: str ='') -> list:
        '''receives the text of the entry or the card buttons and inserts the cards in the list of their respective "owner" '''
        global selected_cards

        # extracts the two cards from the text
        add_card_1 = add_card[0:2]
        add_card_2 = add_card[2:4]
        del_card_1 = del_card[0:2]
        del_card_2 = del_card[2:4]

        # insert the cards in the list
        if add_card_1 and add_card_1 not in selected_cards[owner_cards]:
            selected_cards[owner_cards].append(add_card_1)
        if add_card_2 and add_card_2 not in selected_cards[owner_cards]:
            selected_cards[owner_cards].append(add_card_2)

        # delete the cards from the list
        if del_card_1:
            selected_cards[owner_cards].remove(del_card_1)
        if del_card_2:
            selected_cards[owner_cards].remove(del_card_2)

        print(selected_cards)
        return selected_cards[owner_cards]
            