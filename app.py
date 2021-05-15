import tkinter
from tkinter import ttk
from module import naipes_list, cards_matrix, hands, combinations, default_color_buttons, \
    color_button_control


class PokerRangeAnalysis:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_resizable(False, False) # block window resize
        self.root.title('Poker Range Analysis')
        
        self.widgets = {}
        
        self.create_tabs_layout()
        self.creates_cards_selection_frame(self.root, 1, 0)

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
            'Pré-Flop': {'tab_name': 'pf', 'qtd': 2}, 'Flop': {'tab_name': 'f', 'qtd': 3}, 
            'Turn': {'tab_name': 't', 'qtd': 3}, 'River': {'tab_name': 'r', 'qtd': 3}}

        for street in street_tabs_structure:
            main_frame = tkinter.Frame(self.root)
            path = street_tabs_structure[street]
            self.creates_slot_buttons(main_frame, path['qtd'], path['tab_name'], 0, 0)
            self.creates_equity_frame(main_frame, path['qtd'], 'equity', 0, 1)
            self.creates_equity_frame(main_frame, path['qtd'], 'fold_equity', 0, 2)
            tabs_control.add(main_frame, text = street)
    
    def creates_slot_buttons(self, frame, qtd, abbreviation, row, column):
        buttons_frame = tkinter.Frame(frame)
        buttons_frame.grid(row = row, column = column, sticky = 's', ipady = 7)

        for n in range(qtd):
            slot_name = f'{abbreviation}{n + 1}'
            slot_button = tkinter.Button(buttons_frame, text = slot_name.upper(), width = 10)
            slot_button.config(command = lambda slot_name = slot_name
            :rsw_slots[slot_name].show())
            slot_button.grid(row = n, column = 0, padx = 5, pady = 5, sticky = 's')
            self.widgets[slot_name] = slot_button

    def creates_equity_frame(self, frame, entry_rows, equity_type, frame_row, frame_column):
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

    def creates_cards_selection_frame(self, frame, row, column):
        main_frame = tkinter.Frame(frame, padx = 5, pady = 5, bd = 2, relief = 'groove')
        main_frame.grid(row = row, column = column, padx = 10, pady = 10, columnspan = 3)

        list_labels = ['hero', 'flop', 'turn', 'river']
        img_cards = tkinter.PhotoImage(file = "icons\\card_selection.png", master = main_frame)
        img_clear = tkinter.PhotoImage(file = "icons\\clear_button.png", master = main_frame)

        for i in range(len(list_labels)):
            owner_cards = list_labels[i]
            self.widgets[owner_cards] = {}

            frame = tkinter.Frame(main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{owner_cards.capitalize()}:')
            label.grid(row = 0, column = 0)

            cards_entry = tkinter.Entry(frame, width = 8)
            cards_entry.grid(row = 0, column = 1, padx = 5)
            self.widgets[owner_cards]['entries'] = cards_entry

            choose_cards_button = tkinter.Button(frame, image = img_cards)
            choose_cards_button.image = img_cards  # Keep a reference
            choose_cards_button.grid(row = 0, column = 2, padx = 5, pady = 5)
            choose_cards_button.config(command = lambda owner_cards = owner_cards
                :csw_owners[owner_cards].show())
            self.widgets[owner_cards]['choose_button'] = choose_cards_button

            clear_button = tkinter.Button(frame, image = img_clear)
            clear_button.image = img_clear  # keep a reference
            clear_button.grid(row = 0, column = 3)
            clear_button.config(command = lambda owner_cards = owner_cards: 
                self.clear_button_click(owner_cards))
            self.widgets[owner_cards]['clear_button'] = clear_button

    def fill_cards_entry(self, owner, cards_text):
        self.widgets[owner]['entries'].delete(0, 'end')
        self.widgets[owner]['entries'].insert(0, cards_text)
        return self.widgets[owner]['entries'].get()

    def clear_button_click(self, owner):
        self.widgets[owner]['entries'].delete(0, 'end')
        for card_name in csw_owners[owner].selected_cards[:]:
            card_instance = csw_owners[owner].card_dict[card_name]
            card_instance.deselect_card()
        
        return self.widgets[owner]['entries'].get(), csw_owners[owner].selected_cards

    def show(self):
        self.root.mainloop()
        

class CardSelectionWindow:
    def __init__(self, owner_cards):
        self.owner = owner_cards

        self.wcs = tkinter.Toplevel()
        self.wcs.title(f'Seleção de cartas - {self.owner.capitalize()}')
        self.wcs.wm_resizable(False, False)
        self.wcs.withdraw() # start hidden
        self.wcs.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_click())

        self.selected_cards = []
        self.card_dict = {}
        self.create_layout()

    def create_layout(self):
        main_frame = tkinter.Frame(self.wcs)
        main_frame.grid()

        cards_frame = tkinter.Frame(main_frame)
        cards_frame.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        
        for row in range(4):
            for col in range(13):
                card_name = cards_matrix[row][col]
                card_color = naipes_list[row][1]
                card_instance = Cards(self.owner, card_name, card_color, cards_frame, 
                    row, col)
                self.card_dict[card_name] = card_instance
        
        self.ok_button = tkinter.Button(main_frame, text = 'OK', width = 6, state = 'disabled')
        self.ok_button.config(command = lambda: self.ok_button_click())
        self.ok_button.grid(row = 1, column = 0, pady = (5, 10))

        cancel_button = tkinter.Button(main_frame, text = 'Cancel', width = 6)
        cancel_button.config(command = lambda: self.cancel_button_click())
        cancel_button.grid(row = 1, column = 1, pady = (5, 10))

    def block_used_cards(self):
        blocked_cards = []
        for ow in csw_owners:
            if ow != self.owner: # all owners except the current one
                for card in csw_owners[ow].selected_cards:
                    blocked_cards.append(card)
        
        for card_key in self.card_dict:
            card_instance = self.card_dict[card_key]
            if card_key in blocked_cards:
                card_instance.disable_card_button()
            elif card_instance.get_card_button_state() == 'disabled':
                card_instance.normalize_card_button()
                   
    def show(self):
        self.block_used_cards()
        self.wcs.deiconify()
        return 'the card selection window was displayed'
        
    def get_len_cards(self):
        return len(self.selected_cards)

    def activate_ok_button(self):
        self.ok_button['state'] = 'active'
        return self.ok_button['state']

    def disable_ok_button(self):
        self.ok_button['state'] = 'disabled'
    
    def ok_button_click(self):
        cards_text = ''
        for c in csw_owners[self.owner].selected_cards:
            cards_text += c
        foo = app.fill_cards_entry(self.owner, cards_text)
        self.wcs.withdraw()

        return foo

    def cancel_button_click(self):
        self.wcs.withdraw()


class RangeSelectionWindow:
    def __init__(self, slot_name):
        self.slot_name = slot_name
        self.rsw = tkinter.Toplevel()
        self.rsw.title(f'Seleção de ranges - {self.slot_name.upper()}')
        self.rsw.wm_resizable(False, False)
        self.rsw.withdraw()
        self.rsw.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_click())
        self.widgets = {}
        self.hands_dict = {}
        self.selected_hands = []
        self.selected_combos = 0
        self.total_combos = 0
        self.color_buttons = {}
        self.current_color = ''
        self.create_layout()

    def create_layout(self):
        main_frame = tkinter.Frame(self.rsw)
        main_frame.grid()

        hands_frame = tkinter.Frame(main_frame)
        hands_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        # hands buttons
        hands_index = 0
        for row in range (13):
            for col in range (13):
                hand_name = hands[hands_index]
                hand_combos = len(combinations[hand_name])
                original_hand_color = '#FFE7B5' if 's' in hand_name \
                else '#E7EFF7' if 'o' in hand_name else '#CFDFC7'
                # self.total_combos += hand_combos

                hand_instance = Hands(self.slot_name, hand_name, hand_combos, original_hand_color, 
                hands_frame, row, col)
                hands_index += 1
                self.hands_dict[hand_name] = hand_instance
        
        auxiliary_frame = tkinter.Frame(main_frame)
        auxiliary_frame.grid(row = 0, column = 2, padx = (0, 10), pady = (10, 0), sticky = 'n')

        # color buttons
        for key, value in default_color_buttons.items():
            color_button = tkinter.Button(auxiliary_frame, 
                width = 4, text = key, bg = value['color'])
            color_button.config(command = lambda color_button = color_button
                :self.color_button_clicked(color_button))
            color_button_control[self.slot_name]['buttons'].append(color_button)
            color_button.grid(pady = 2)
            self.color_buttons[key] = color_button

        clear_button = tkinter.Button(auxiliary_frame, text = 'Clear')
        clear_button.grid(pady = (5, 20))
        clear_button.config(command = self.clear_button_click)

        if self.slot_name in ('pf1', 'f1', 'f2', 't1', 't2', 'r1', 'r2'):
            next_slot_button = tkinter.Button(auxiliary_frame, text = 'Next Slot')
            next_slot_button.grid(pady = (0, 10))
            next_slot_button.config(command = self.next_slot_button_click)
            self.widgets['next_slot'] = next_slot_button

        if self.slot_name in ('pf2', 'f2', 'f3', 't2', 't3'):
            next_street_button = tkinter.Button(auxiliary_frame, text = 'Next Street')
            next_street_button.grid(pady = (0, ))
            next_street_button.config(command = self.next_street_button_click)
            self.widgets['next_street'] = next_street_button

        # labels
        labels_frame = tkinter.Frame(main_frame)
        labels_frame.grid(row = 1, column = 0, pady = (0 , 5))

        self.label_combo = tkinter.Label(labels_frame) # update_label_combo
        self.label_combo.grid()

    def block_unused_hands(self):
        keys = list(rsw_slots)
        current_slot_index = keys.index(self.slot_name)

        previous_slot = keys[current_slot_index - 1]
        if current_slot_index != 0 and rsw_slots['pf1'].selected_hands == []:
            for hand in self.hands_dict:
                self.hands_dict[hand].button['state'] = 'disabled'
                self.hands_dict[hand].button['bg'] = 'Systembuttonface'
        elif current_slot_index != 0:
            for hand in self.hands_dict:
                if hand not in rsw_slots[previous_slot].selected_hands:
                    self.hands_dict[hand].button['state'] = 'disabled'
                    self.hands_dict[hand].button['bg'] = 'Systembuttonface'
                else:
                    self.hands_dict[hand].button['state'] = 'normal'
                    self.hands_dict[hand].button['bg'] = self.hands_dict[hand].original_hand_color
        else:
            return 'this is the first slot'

    def count_total_combos(self):
        for hand in self.hands_dict:
            if self.hands_dict[hand].button['state'] == 'normal':
                self.total_combos += self.hands_dict[hand].hand_combos

    def show(self):
        self.block_unused_hands()
        self.count_total_combos()
        self.update_label_combo()
        self.rsw.deiconify()
        return 'the range selection window was displayed'

    def cancel_button_click(self):
        self.rsw.withdraw()

    def color_button_clicked(self, color_button):
        if color_button['relief'] == 'raised':
            color_button['relief'] = 'sunken'
            
            # updates the variable that controls the current color
            self.current_color = color_button['bg']

            return color_button['relief'], self.deselect_other_color_buttons(color_button['text'])
            
        elif color_button['relief'] == 'sunken':
            color_button['relief'] = 'raised'
            self.current_color = ''

        return 

    def deselect_other_color_buttons(self, color_button_name):
        for key in self.color_buttons:
            if key != color_button_name:
                self.color_buttons[key]['relief'] = 'raised'

        return 'all other color buttons have been deselected'

    def update_label_combo(self):
        if self.total_combos == 0:
            self.percent_hands_selected = 0
        else:
            self.percent_hands_selected = (self.selected_combos / self.total_combos) * 100
        self.label_combo.config(
            text = f'Leque de mãos selecionado contém '\
                f'{self.selected_combos}/{self.total_combos} mãos ({self.percent_hands_selected:.2f}%)')

    def clear_button_click(self):
        for hand in self.selected_hands[:]:
            self.hands_dict[hand].deselect_hand()

    def next_slot_button_click(self):
        self.rsw.withdraw()
        keys = list(rsw_slots)
        next_slot = keys[(keys.index(self.slot_name)) + 1]
        rsw_slots[next_slot].show()

        return next_slot

    def next_street_button_click(self):
        self.rsw.withdraw()
        keys = list(rsw_slots)

        current_slot_first_char = keys[keys.index(self.slot_name)][0]
        next_slot_first_char = keys[((keys.index(self.slot_name)) + 1)][0]

        if next_slot_first_char == current_slot_first_char:
            next_street = keys[keys.index(self.slot_name) + 2]
        else:
            next_street = keys[keys.index(self.slot_name) + 1]

        rsw_slots[next_street].show()

        return next_street


class Cards:
    def __init__(self, owner_cards, card_name, card_color, frame, row, column):
        self.owner = owner_cards
        self.card_name = card_name
        self.card_color = card_color
        self.frame = frame
        self.row = row
        self.column = column
        self.button = ''
        self.create_button()

    def create_button(self):
        card_button = tkinter.Button(self.frame, width = 2, heigh = 2, 
            text = self.card_name, fg = self.card_color)
        card_button.config(command = lambda: self.card_button_click())
        card_button.grid(row = self.row, column = self.column)
        self.button = card_button
        return card_button

    def get_card_button_state(self):
        state = self.button['state']
        return state

    def card_button_click(self):
        self.card_window = csw_owners[self.owner] # card selection window
        qtd = self.card_window.get_len_cards()

        if self.button['state'] == 'normal':
            if self.button['bg'] == 'SystemButtonFace':
                if self.owner == 'hero' and qtd < 2:
                    return self.select_card()
                elif self.owner == 'flop' and qtd < 3:
                    return self.select_card()
                elif (self.owner == 'turn' or self.owner == 'river') and qtd == 0:
                    return self.select_card()
            else:
                return self.deselect_card()
        elif self.button['state'] == 'disabled':
            return "button can't be clicked"

    def select_card(self):
        self.card_window = csw_owners[self.owner] # card selection window
        self.button['bg'] = 'gray'
        self.card_window.selected_cards.append(self.card_name)

        qtd = self.card_window.get_len_cards()

        if self.owner == 'hero' and qtd == 2:
            self.card_window.activate_ok_button()
        elif self.owner == 'flop' and qtd == 3:
            self.card_window.activate_ok_button()
        elif (self.owner == 'turn' or self.owner == 'river') and qtd == 1:
            self.card_window.activate_ok_button()

        return csw_owners[self.owner].selected_cards, self.card_window.ok_button['state']

    def deselect_card(self):
        self.card_window = csw_owners[self.owner] # card selection window
        self.button['bg'] = 'SystemButtonFace'
        self.card_window.selected_cards.remove(self.card_name)

        qtd = self.card_window.get_len_cards()

        if self.owner == 'hero' and qtd < 2:
            self.card_window.disable_ok_button()
        elif self.owner == 'flop' and qtd < 3:
            self.card_window.disable_ok_button()
        elif (self.owner == 'turn' or self.owner == 'river') and qtd < 1:
            self.card_window.disable_ok_button()
        
        return csw_owners[self.owner].selected_cards, self.card_window.ok_button['state']

    def normalize_card_button(self):
        self.button['state'] = 'normal'

    def disable_card_button(self):
        self.button['state'] = 'disabled'


class Hands:
    def __init__(self, slot_name, hand_name, hand_combos, original_hand_color, frame, row, column):
        self.slot_name = slot_name
        self.hand_name = hand_name
        self.hand_combos = hand_combos
        self.hand_full_name = f'{hand_name}\n{hand_combos}'
        self.original_hand_color = original_hand_color
        self.frame = frame
        self.row = row
        self.column = column
        self.button = ''
        self.create_hand_button()

    def create_hand_button(self):
        hand_button = tkinter.Button(self.frame, width = 5, bg = self.original_hand_color, 
            text = self.hand_full_name)
        hand_button.config(command = lambda: self.hand_button_clicked())
        hand_button.grid(row = self.row, column = self.column)
        self.button = hand_button

    def hand_button_clicked(self):
        self.current_color = rsw_slots[self.slot_name].current_color

        if self.current_color != '' and self.button['bg'] == self.original_hand_color:
            return self.select_hand()
        elif self.current_color != '' and self.button['bg'] != self.current_color:
            return self.reselect_hand()
        elif (self.button['bg'] == self.current_color) or (self.current_color == '' and \
            self.button['bg'] != self.original_hand_color):
            return self.deselect_hand()
        
        return 'nothin has been changed'
    
    def select_hand(self):
        self.button['bg'] = self.current_color
        rsw_slots[self.slot_name].selected_combos += self.hand_combos
        rsw_slots[self.slot_name].selected_hands.append(self.hand_name)
        rsw_slots[self.slot_name].update_label_combo()

    def reselect_hand(self):
        self.button['bg'] = self.current_color

    def deselect_hand(self):
        self.button['bg'] = self.original_hand_color
        rsw_slots[self.slot_name].selected_combos -= self.hand_combos
        rsw_slots[self.slot_name].selected_hands.remove(self.hand_name)
        rsw_slots[self.slot_name].update_label_combo()


'''----------------------------------------------------------------------------------------------- '''
app = PokerRangeAnalysis()

# add topleves to the dicionary created earlier (module.py)
csw_owners = {'hero': CardSelectionWindow('hero'), 'flop': CardSelectionWindow('flop'), 
    'turn': CardSelectionWindow('turn'), 'river': CardSelectionWindow('river'), }

# creates the range selection window for each street
rsw_slots = {'pf1': RangeSelectionWindow('pf1'), 'pf2': RangeSelectionWindow('pf2'), 
    'f1': RangeSelectionWindow('f1'),'f2': RangeSelectionWindow('f2'),'f3': RangeSelectionWindow('f3'),
    't1': RangeSelectionWindow('t1'), 't2': RangeSelectionWindow('t2'), 't3': RangeSelectionWindow('t3'), 
    'r1': RangeSelectionWindow('r1'), 'r2': RangeSelectionWindow('r2'), 'r3': RangeSelectionWindow('r3')}

pf_selected_color = ''


if __name__ == '__main__':
    app.show()
