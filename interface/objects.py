import tkinter
import itertools
from pprint import pprint

current_color_button_name = ''

selected_cards = {'Hero':[], 'Flop':[], 'Turn':[], 'River':[]}

figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
naipes_list = [('d','#014082'), ('h','#CC0000'), ('s','#000000'), ('c','#00732B')]
cards = [[figure + naipe[0] for figure in figures_list] for naipe in naipes_list]
hands = []
pairs = []
suiteds = []
off_suiteds = []
combinations = {}

removed_combinations = {}

for f1 in figures_list:
    for f2 in figures_list:
        if f1 == f2:
            hands.append(f1+f2)
        elif figures_list.index(f1) < figures_list.index(f2):
            hands.append(f1+f2+'s')
        else:
            hands.append(f2+f1+'o')

naipes = "dhsc"
for hand in hands:
    if hand[0] == hand[1]:
        pairs.append(hand)
    elif 's' in hand:
        suiteds.append(hand)
    elif 'o' in hand:
        off_suiteds.append(hand)

for hand in pairs:
    combinations[hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
    for naipe in itertools.combinations(naipes, len(hand))]

for hand in suiteds:
    combinations[hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
    for naipe in list(itertools.product(naipes, repeat=2))]

# gambiarra pra deixar somente as mãos suited
for hand in suiteds:
    for combo in combinations[hand][:]:
        if combo[0][1] != combo[1][1]:
            combinations[hand].remove(combo)

for hand in off_suiteds:
    combinations[hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
    for naipe in list(itertools.product(naipes, repeat=2))]

# gambiarra pra deixar somente as mãos 0ff-suiteds
for hand in off_suiteds:
    for combo in combinations[hand][:]:
        if combo[0][1] == combo[1][1]:
            combinations[hand].remove(combo)

select_hands_total_combo = 0
streets_labels_dict = {}
streets_ranges_control = {}

# ----------------------------------------------------------------------------------------------------

class FrameStreetsButtons:
    def __init__(self, master, qtd, name, row, column):
        self.qtd = qtd
        self.name = name
        self.row = row
        self.column = column

        frame_buttons = tkinter.Frame(master)
        frame_buttons.grid(row = self.row, column = self.column, sticky = 's', ipady = 7)
    
        for n in range(self.qtd):
            button_name = f'{self.name}{n + 1}'
            button = tkinter.Button(frame_buttons, text = button_name, width = 10)
            button.config(command = lambda button = button: WindowRangeSelection(button))
            button.grid(row = n, column = 0, padx = 5, pady = 5, sticky = 's')
            streets_ranges_control[button_name] = {
                'caller_button': button, 
                'range_detail': {
                    'RF+': {'color': '#B2301E'}, 'RFF': {'color' : '#BE6EAE'}, 'RF-': {'color': '#EA8376'}, 
                    'RM+': {'color': '#4572A9'}, 'RM-': {'color': '#81ACDF'}, 'RF': {'color': '#E8950F'},
                    'RF-': {'color': '#FFCD69'}, 'SPLIT': {'color': '#27A2A1'}
                }
            }

class FrameStreetsEquity:
    def __init__(self, master, street, rows, table_type, row, column):
        self.street = street
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
            foo = str(f'{title_dict[self.table_type][i]}').replace('\n', '_').replace('. ', '_').replace('_(%)', '')
            for x in range(self.rows):
                label = tkinter.Label(range_frame, width = 8, relief = 'groove', bg = 'white')
                label.grid(row = x + 1, column = i, padx = 5, pady = 7)
                streets_labels_dict[f'{street}{x+1}_{foo}'] = label
        
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
        CardsAndHands().selected_card(label_name, add_card = '', del_card = entry.get())
        entry.delete(0, 'end')
        button_choose['state'] = 'active'
        # selected_cards[label_name] = []
        print(selected_cards)

class WindowRangeSelection:
    def __init__(self, caller_button: object):
        # print(caller_button['text'])
        # streets_ranges_control['PF1']['range_detail']['RF+']['color'] = 'black'
        # pprint(streets_ranges_control)
        self.caller_button = caller_button
        self.caller_button['state'] = 'disabled'

        self.range_window = tkinter.Toplevel()
        self.range_window.title(f"Selecione o Range - {caller_button['text']}")
        self.range_window.wm_resizable('false', 'false')
        self.range_window.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_click(self.range_window, self.caller_button))

        self.create_hand_buttons_matrix(self.range_window, 0, 0, caller_button)
        self.creates_auxiliary_buttons(self.range_window, 0, 1, self.caller_button['text'])
        self.creates_space_comments(self.range_window, 2, 0)
        self.creates_ok_and_cancel_buttons(self.range_window, 3, 0)
        self.check_range_pre_selected(self.caller_button['text'])

    def create_hand_buttons_matrix(self, master, row, column, street_name):
        self.row = row
        self.column = column
        self.street_name = street_name
        self.range_buttons = [[None for x in range(13)] for x in range (13)]

        global select_hands_total_combo
        select_hands_total_combo = 0

        cards_frame = tkinter.Frame(master)
        cards_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10)
        hands_index = 0
        self.card_buttons_dict = {}
        self.total_combinations = 0
        for row in range (13):
            for col in range (13):
                hand_button_pre_name = hands[hands_index]
                hand_button_n_combos = len(combinations[hand_button_pre_name])
                hand_button_name = f'{hand_button_pre_name}\n{hand_button_n_combos}'
                original_color = '#FFE7B5' if 's' in hand_button_name else '#E7EFF7' if 'o' in hand_button_name else '#CFDFC7'

                hand_button = self.range_buttons[row][col] = tkinter.Button(cards_frame, width = 5, bg = original_color, text = hand_button_name)
                hand_button.grid(row = row, column = col)
                hand_button.config(command = lambda hand_button = hand_button, hand_button_pre_name = hand_button_pre_name, original_color = original_color: self.select_hand(hand_button, hand_button_pre_name, original_color, street_name['text']))

                self.card_buttons_dict[hand_button_pre_name] = (hand_button, original_color)
                hands_index += 1
                self.total_combinations += hand_button_n_combos
        
    def creates_auxiliary_buttons(self, master, row, column, current_street):
        """Cria os botões auxiliares de cor, limpar e próximo slot

        Args:
            master (object): local onde o frame será apresentado
            row (interger): linha onde o frame será apresentado
            column (interger): coluna onde o frame será apresentado
            current_street (str): nome da street atual
        """

        self.row = row
        self.column = column
        self.current_street = current_street
        # print(current_street)

        frame_auxiliary = tkinter.Frame(master)
        frame_auxiliary.grid(row = self.row, column = self.column, padx = 5)

        button_clear = tkinter.Button(frame_auxiliary, text = 'Limpar', command = lambda: self.clear_hands(self.caller_button))
        button_clear.grid(padx = 5, pady = 20)

        # streets_ranges_control[current_street]['range_detail']['test'] = []

        # pprint(streets_ranges_control)
        for key, value in streets_ranges_control[current_street]['range_detail'].items():
            color_button = tkinter.Button(frame_auxiliary, width = 4, text = key, bg =  value['color'])
            color_button.grid(pady = 5)
            color_button.config(command = lambda key = key: self.pick_color(key, self.current_street))

            range_color_label = tkinter.Label(frame_auxiliary, text = 0)
            range_color_label.grid()

            value['button'] = color_button
            value['label'] = range_color_label
        # pprint(streets_ranges_control[current_street])

        next_slot_button = tkinter.Button(frame_auxiliary, text = 'Próximo Slot', command = lambda: self.next_slot_click(self.range_window, self.caller_button))
        next_slot_button.grid(pady = 30)

    def creates_space_comments(self, master, row, column):
        self.row = row
        self.column = column

        frame_comments = tkinter.Frame(master)  
        frame_comments.grid(row = self.row, column = self.column, padx = 5, pady = 5)
        self.label_combo_count = tkinter.Label(frame_comments, text = f'Leque de mãos selecionado contém {select_hands_total_combo}/{self.total_combinations} mãos (0.00%)')
        self.label_combo_count.grid(row = 0, column = 0, pady = 5)
        # label_comments = tkinter.Label(frame_comments, text = 'Comentários')
        # label_comments.grid(row = 1, column = 0, sticky = 'w')
        # text_box = tkinter.Text(frame_comments, width = 72, height = 5)
        # text_box.grid(row = 2, column = 0, padx = 5, pady = 5)

    def creates_ok_and_cancel_buttons(self, master, row, column):
        self.row = row
        self.column = column

        frame_buttons = tkinter.Frame(master)
        frame_buttons.grid(row = self.row, column = self.column, padx = 5, pady = 5)
        ok_button = tkinter.Button(frame_buttons, text = 'OK', width = 6, command = lambda: self.ok_button_click(self.range_window, self.caller_button))
        ok_button.grid(row = 0, column = 0, padx = 5, pady = 5)
        cancel_button = tkinter.Button(frame_buttons, text = 'Cancel', width = 6, command = lambda: self.cancel_button_click(self.range_window, self.caller_button))
        cancel_button.grid(row = 0, column = 1, padx = 5, pady = 5)

    def check_range_pre_selected(self, current_street):
        path = streets_ranges_control[current_street]['range_detail']
        for key, value in path.items():
            if 'selected_range' in path[key] and path[key]['selected_range']:
                # print(key, path[key]['selected_range'])
                if path[key]['button']['relief'] == 'raised':
                    self.pick_color(key, current_street)
                for hand in value['selected_range'][:]:
                    self.select_hand(self.card_buttons_dict[hand][0], str(hand), self.card_buttons_dict[hand][1], current_street)
    
    def ok_button_click(self, top_level: object, caller_button: object):
        global select_hands_total_combo, streets_labels_dict

        street = caller_button['text']
        streets_labels_dict[f'{street}_Range_(mãos)']['text'] = select_hands_total_combo

        top_level.destroy()
        caller_button['state'] = 'active'
    
    def cancel_button_click(self, top_level: object, caller_button: object):
        top_level.destroy()
        caller_button['state'] = 'active'

    def select_hand(self, hand_button, hand_button_name, original_color, street_name):
        """if any color button is selected, when clicking on the card button, its color is changed

        Args:
            hand_button (object): botão referente a cada mão
            hand_button_name (str): nome (texto) do botão
            color (str): código da cor
        """
        global current_color_button_name, select_hands_total_combo

        path = streets_ranges_control[street_name]['range_detail'][current_color_button_name]

        if current_color_button_name and hand_button['bg'] == original_color:
            hand_button['bg'] = path['color']

            select_hands_total_combo += len(combinations[hand_button_name])
            percentual = (select_hands_total_combo / self.total_combinations) * 100
            self.label_combo_count['text'] = f'Leque de mãos selecionado contém {select_hands_total_combo}/{self.total_combinations} mãos ({percentual:.2f}%)'
            
            path['label']['text'] += len(combinations[hand_button_name])
            # print(streets_ranges_control['T2']['range_detail'][current_color_button_name]['label']['text'])

            # adiciona a mão selecionada no range da street específica e da cor específica
            if 'selected_range' not in path:
                path['selected_range'] = []
                # pprint(streets_ranges_control)

                if hand_button_name not in path['selected_range']:
                    path['selected_range'].append(hand_button_name)
                    # pprint(streets_ranges_control)
            elif hand_button_name not in path['selected_range']:
                path['selected_range'].append(hand_button_name)
            # pprint(streets_ranges_control)

            # if 'combo_color_range' not in path:
            #     # streets_ranges_control[street_name]['range_detail'][current_color_button_name]['combo_color_range'] = 0
            #     path['combo_color_range'] = path['label']['text']
            #     # print(street_name, current_color_button_name, streets_ranges_control['PF1']['range_detail']['RF+'])
            # else:
            #     path['combo_color_range'] = path['label']['text']

        elif current_color_button_name and hand_button['bg'] == path['button']['bg']:
            hand_button.config(bg = original_color)

            select_hands_total_combo -= len(combinations[hand_button_name])
            percentual = (select_hands_total_combo / self.total_combinations) * 100
            self.label_combo_count['text'] = f'Leque de mãos selecionado contém {select_hands_total_combo}/{self.total_combinations} mãos ({percentual:.2f}%)'
            
            path['label']['text'] -= len(combinations[hand_button_name])
            path['selected_range'].remove(hand_button_name)
            # print(street_name, current_color_button_name, streets_ranges_control['PF1']['range_detail']['RF+']['selected_range'])
        # pprint(streets_ranges_control)

    def pick_color(self, color_button_name: object, current_street):
        global current_color_button_name

        path = streets_ranges_control[current_street]['range_detail']

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
        # pprint(streets_ranges_control)

    def clear_hands(self, current_street):
        global current_color_button_name, select_hands_total_combo
        self.check_range_pre_selected(current_street['text'])

        path = streets_ranges_control[current_street['text']]['range_detail']

        for color_button_name in path:
            path[current_color_button_name]['button']['relief'] = 'raised'
        current_color_button_name = ''

    def next_slot_click(self, top_level: object, caller_button: object):
        self.ok_button_click(top_level, caller_button)

        streets_buttons_list = list(streets_ranges_control)
        next_button = streets_buttons_list[streets_buttons_list.index(caller_button['text']) + 1]
        WindowRangeSelection(streets_ranges_control[next_button]['caller_button'])
        # self.check_range_pre_selected('PF1')

class WindowCardSelection:
    def __init__(self, owner_cards:str, caller_button:object, entry:object) -> object:
        pprint(streets_ranges_control)
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
            self.removes_combos(add_card_1)
        if add_card_2 and add_card_2 not in selected_cards[owner_cards]:
            selected_cards[owner_cards].append(add_card_2)
            self.removes_combos(add_card_2)

        # delete the cards from the list
        if del_card_1:
            selected_cards[owner_cards].remove(del_card_1)
            self.re_add_combos(del_card_1, owner_cards)
        if del_card_2:
            selected_cards[owner_cards].remove(del_card_2)
            self.re_add_combos(del_card_2, owner_cards)

        return selected_cards[owner_cards]

    def removes_combos(self, card):
        '''removes all combinations of hands using this card'''

        # print('combinations', combinations['AA'])
        # create a dictionary with the combinations that will be deleted
        for hand in combinations:
            for combo in combinations[hand]:
                if card in combo[0] or card in combo[1]:
                    if hand not in removed_combinations:
                        removed_combinations[hand] = []
                        removed_combinations[hand].append(combo)
                    elif hand in removed_combinations and combo not in removed_combinations[hand]:
                        removed_combinations[hand].append(combo)
        # print('removed combinations', removed_combinations['AA'])

        # deletes combinations from the original dictionary
        for hand in removed_combinations:
            for combo in removed_combinations[hand]:
                if combo in combinations[hand]:
                    combinations[hand].remove(combo)
        # print('combinations', combinations['AA'])

    def re_add_combos(self, card, owner_cards):
        ''' when you deselect a card, all combos of that card are returned to the main dictionary'''

        locked_cards = []
        for owner_cards in selected_cards:
            for c in selected_cards[owner_cards]:
                locked_cards.append(c)
        # print('locked card', locked_cards)
        # print('combinations', combinations['AA'])
        # print('selected cards', selected_cards)

        # based on the auxiliary dictionary, re-add combos from the main dictionary
        for hand in removed_combinations:
            for combo in removed_combinations[hand]:
                if (card in combo[0] and combo[1] not in locked_cards) or (card in combo[1] and combo[0] not in locked_cards):
                        combinations[hand].append(combo)
        
        # after re-add in main dictionary, it also removes combos from the auxiliary dictionary
        for hand in removed_combinations:
            for combo in list(removed_combinations[hand]): # way to remove items from a dictionary by iterating over it
                if (card in combo[0] and combo[1] not in locked_cards) or (card in combo[1] and combo[0] not in locked_cards):
                    removed_combinations[hand].remove(combo)
        # print('combinations AA', combinations['AA'])
        # print('removed combinations', removed_combinations['AA'])