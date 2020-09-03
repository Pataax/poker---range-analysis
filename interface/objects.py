import tkinter



current_color = ''

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

        for i in range (len(labels_list)):
            frame = tkinter.Frame(main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{labels_list[i]}:')
            label.grid(row = 0, column = 0)

            entry = tkinter.Entry(frame, width = 5)
            entry.grid(row = 0, column = 1, padx = 5)

            button_choose = tkinter.Button(frame, width = 2, height = 1, 
                command = WindowCardSelection)
            button_choose.grid(row = 0, column = 2, padx = 5, pady = 5)

            button_clear = tkinter.Button(frame, width = 2)
            button_clear.grid(row = 0, column = 3)

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
                    color = color: self.select_card(hand_button, color))
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

    def select_card(self, card_button, color):
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
    def __init__(self):
        window_card_selection = tkinter.Toplevel()
        window_card_selection.title('Card Selection')

        main_frame = tkinter.Frame(window_card_selection)
        main_frame.grid(padx = 10, pady = 10)

        cards_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        naipes_list = ['d','h','s','c']

        for c in range(len(cards_list)):
            for n in range(len(naipes_list)):
                card_button = tkinter.Button(main_frame, width = 2, heigh = 2,
                    text = f'{cards_list[c]}{naipes_list[n]}')
                card_button.grid(row = n, column = c, padx = 1, pady = 1)