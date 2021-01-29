import tkinter, itertools
from pprint import pprint
from tkinter import ttk

from interface.objects import FrameBasicInformations, FrameOpponentInformations, FrameNotesAndInfos, FrameStreetsSelectCards


class PokerRangeAnalysis:
    def __init__(self, master):
        self.master = master
        self.master.title('Poker Range Analysis')
        self.creates_tab_control(master)
        self.creates_tabs_layouts(self.tab_control)
        self.creates_cards_combinations()

        # global select_hands_total_combo
        # select_hands_total_combo = 0
        
    def creates_tab_control(self, master):
        self.tab_control = ttk.Notebook(master)
        self.tab_control.grid(padx = 5, pady = 5)

    def creates_tabs_layouts(self, tab_control):
        # Tab Start
        tab_start = ttk.Frame(tab_control, width = 546, height = 210)
        tab_control.add(tab_start, text="Início")
        FrameBasicInformations(tab_start)
        FrameOpponentInformations(tab_start)
        FrameNotesAndInfos(tab_start)

        global main_dict
        main_dict = {
                    'streets': {
                        'Pré-Flop': {'tab_name': 'PF', 'qtd': 2}, 'Flop': {'tab_name': 'F', 'qtd': 3}, 
                        'Turn': {'tab_name': 'T', 'qtd': 3}, 'River': {'tab_name': 'R', 'qtd': 3}
                        }, 
                    'hands': [],
                    'combinations': {}
                    }

        # Others tabs
        for street in main_dict['streets']:
            main_frame = tkinter.Frame()
            path = main_dict['streets'][street]

            FrameStreetsButtons(main_frame, street, path['qtd'], path['tab_name'], 0, 0)
            FrameStreetsEquity(main_frame, path['tab_name'], path['qtd'], 'equity', 0, 1)
            FrameStreetsEquity(main_frame, path['tab_name'], path['qtd'], 'fold_equity', 0, 2)
            FrameStreetsSelectCards(root, 1, 0)
            self.tab_control.add(main_frame, text = street)

    def creates_cards_combinations(self):
        figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        naipes_list = [('d','#014082'), ('h','#CC0000'), ('s','#000000'), ('c','#00732B')]
        cards = [[figure + naipe[0] for figure in figures_list] for naipe in naipes_list]

        pairs = []
        suiteds = []
        off_suiteds = []

        for f1 in figures_list:
            for f2 in figures_list:
                if f1 == f2:
                    main_dict['hands'].append(f1+f2)
                elif figures_list.index(f1) < figures_list.index(f2):
                    main_dict['hands'].append(f1+f2+'s')
                else:
                    main_dict['hands'].append(f2+f1+'o')

        naipes = "dhsc"
        for hand in main_dict['hands']:
            if hand[0] == hand[1]:
                pairs.append(hand)
            elif 's' in hand:
                suiteds.append(hand)
            elif 'o' in hand:
                off_suiteds.append(hand)

        for hand in pairs:
            main_dict['combinations'][hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
            for naipe in itertools.combinations(naipes, len(hand))]

        for hand in suiteds:
            main_dict['combinations'][hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
            for naipe in list(itertools.product(naipes, repeat=2))]

        # gambiarra pra deixar somente as mãos suited
        for hand in suiteds:
            for combo in main_dict['combinations'][hand][:]:
                if combo[0][1] != combo[1][1]:
                    main_dict['combinations'][hand].remove(combo)

        for hand in off_suiteds:
            main_dict['combinations'][hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
            for naipe in list(itertools.product(naipes, repeat=2))]

        # gambiarra pra deixar somente as mãos 0ff-suiteds
        for hand in off_suiteds:
            for combo in main_dict['combinations'][hand][:]:
                if combo[0][1] == combo[1][1]:
                    main_dict['combinations'][hand].remove(combo)

class FrameStreetsButtons:
    def __init__(self, master, street, qtd, btn_name, row, column):
        self.street = street
        self.qtd = qtd
        self.btn_name = btn_name
        self.row = row
        self.column = column

        frame_buttons = tkinter.Frame(master)
        frame_buttons.grid(row = self.row, column = self.column, sticky = 's', ipady = 7)
    
        for n in range(self.qtd):
            button_name = f'{self.btn_name}{n + 1}'
            button = tkinter.Button(frame_buttons, text = button_name, width = 10)
            button.config(command = lambda button = button: WindowRangeSelection(button))
            button.grid(row = n, column = 0, padx = 5, pady = 5, sticky = 's')
            main_dict['streets'][street][button_name] = {
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
                # streets_labels_dict[f'{street}{x+1}_{foo}'] = label

class WindowRangeSelection:
    def __init__(self, caller_button: object):
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
                hand_button_pre_name = main_dict['hands'][hands_index]
                hand_button_n_combos = len(main_dict['combinations'][hand_button_pre_name])
                hand_button_name = f'{hand_button_pre_name}\n{hand_button_n_combos}'
                original_color = '#FFE7B5' if 's' in hand_button_name else '#E7EFF7' if 'o' in hand_button_name else '#CFDFC7'

                hand_button = self.range_buttons[row][col] = tkinter.Button(cards_frame, width = 5, bg = original_color, text = hand_button_name)
                hand_button.grid(row = row, column = col)
                if hand_button_n_combos == 0:
                    hand_button['state'] = 'disabled'
                hand_button.config(command = lambda hand_button = hand_button, hand_button_pre_name = hand_button_pre_name, original_color = original_color: self.select_hand(hand_button, hand_button_pre_name, original_color, street_name['text']))

                self.card_buttons_dict[hand_button_pre_name] = (hand_button, original_color)
                hands_index += 1
                self.total_combinations += hand_button_n_combos
        
    def creates_auxiliary_buttons(self, master, row, column, current_street):
        """Cria os botões auxiliares de cor, limpar e próximo slot"""

        self.row = row
        self.column = column
        self.current_street = current_street

        frame_auxiliary = tkinter.Frame(master)
        frame_auxiliary.grid(row = self.row, column = self.column, padx = 5)

        button_clear = tkinter.Button(frame_auxiliary, text = 'Limpar', command = lambda: self.clear_hands(self.caller_button))
        button_clear.grid(padx = 5, pady = 20)

        # streets_ranges_control[current_street]['range_detail']['test'] = []

        for key, value in streets_ranges_control[current_street]['range_detail'].items():
            color_button = tkinter.Button(frame_auxiliary, width = 4, text = key, bg =  value['color'])
            color_button.grid(pady = 5)
            color_button.config(command = lambda key = key: self.pick_color(key, self.current_street))

            range_color_label = tkinter.Label(frame_auxiliary, text = 0)
            range_color_label.grid()

            value['button'] = color_button
            value['label'] = range_color_label

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
        
        # calcula  a equidade do vilão
        path = streets_ranges_control[street]['range_detail']
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

            streets_labels_dict[f'{street}_Split']['text'] = f'{(split / select_hands_total_combo) * 100:.2f}%'
            streets_labels_dict[f'{street}_Eq_Hero']['text'] = f'{((range_fraco + range_medio / 2 )/ select_hands_total_combo) * 100:.2f}%'
            streets_labels_dict[f'{street}_Eq_Vilão']['text'] = f'{((range_forte + range_medio / 2) / select_hands_total_combo) * 100:.2f}%'
        
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

        if current_color_button_name: # apenas se alguma cor estiver selecionada
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

        # automaticamente deseleciona todas as cartas
        self.check_range_pre_selected(current_street['text'])


        # esquema para deselecionar os botoes de cor e limpar o current color
        path = streets_ranges_control[current_street['text']]['range_detail']

        for color_button_name in path:
            path[color_button_name]['button']['relief'] = 'raised'
        current_color_button_name = ''

    def next_slot_click(self, top_level: object, caller_button: object):
        self.ok_button_click(top_level, caller_button)

        # encontra a próxima street
        streets_buttons_list = list(streets_ranges_control)
        next_button = streets_buttons_list[streets_buttons_list.index(caller_button['text']) + 1]

        # copia os ranges da street atual para a proxima street
        old_path = streets_ranges_control[caller_button['text']]['range_detail']
        new_path = streets_ranges_control[next_button]['range_detail']
        for key in old_path:
            if 'selected_range' in old_path[key]:
                new_path[key]['selected_range'] = old_path[key]['selected_range']

        # abre a janela da proxima street
        WindowRangeSelection(streets_ranges_control[next_button]['caller_button'])

class CardsAndHands:
    def selected_card(self, owner_cards:str, add_card:str, del_card: str ='') -> list:
        '''receives the text of the entry or the card buttons and inserts the cards in the list of their respective "owner" '''
        global selected_cards

        # extracts the two cards from the text
        add_card_1 = add_card[0:2]
        add_card_2 = add_card[2:4]
        add_card_3 = add_card[4:6]
        del_card_1 = del_card[0:2]
        del_card_2 = del_card[2:4]
        del_card_3 = del_card[4:6]

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

if __name__ == '__main__':
    root = tkinter.Tk()
    root.wm_resizable(False, False)
    PokerRangeAnalysis(root)
    root.mainloop()
