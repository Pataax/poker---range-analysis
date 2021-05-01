import tkinter
from tkinter import ttk
from pprint import pprint
from module import naipes_list, cards_matrix, hands, default_color_buttons, \
    color_button_control, csw_owners


class PokerRangeAnalysis:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_resizable(False, False) # block window resize
        self.root.title('Poker Range Analysis')
        self.create_tabs_layout()
        self.creates_cards_seletion_frame(self.root, 1, 0)

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
            main_frame = tkinter.Frame()
            path = street_tabs_structure[street]
            self.creates_slot_buttons(main_frame, street , path['qtd'], path['tab_name'], 0, 0)
            self.creates_equity_frame(main_frame, path['qtd'], 'equity', 0, 1)
            self.creates_equity_frame(main_frame, path['qtd'], 'fold_equity', 0, 2)
            tabs_control.add(main_frame, text = street)
    
    def creates_slot_buttons(self, frame, street, qtd, abbreviation:str, row, column):
        buttons_frame = tkinter.Frame(frame)
        buttons_frame.grid(row = row, column = column, sticky = 's', ipady = 7)

        for n in range(qtd):
            slot_name = f'{abbreviation}{n + 1}'
            slot_button = tkinter.Button(buttons_frame, text = slot_name.upper(), width = 10)
            slot_button.config(command = lambda slot_name = slot_name
            :rsw_slots[slot_name].show())
            slot_button.grid(row = n, column = 0, padx = 5, pady = 5, sticky = 's')

    def creates_equity_frame(self, frame, entry_rows:str, equity_type:str, frame_row, frame_column):
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

    def creates_cards_seletion_frame(self, frame, row, column):
        main_frame = tkinter.Frame(frame, padx = 5, pady = 5, bd = 2, relief = 'groove')
        main_frame.grid(row = row, column = column, padx = 10, pady = 10, columnspan = 3)

        list_labels = ['hero', 'flop', 'turn', 'river']
        img_cards = tkinter.PhotoImage(file = 'icons/card_selection.png')
        img_clear = tkinter.PhotoImage(file = 'icons/button_clear.png')

        for i in range(len(list_labels)):
            owner_cards = list_labels[i]

            frame = tkinter.Frame(main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{owner_cards.capitalize()}:')
            label.grid(row = 0, column = 0)

            cards_entry = tkinter.Entry(frame, width = 8)
            cards_entry.grid(row = 0, column = 1, padx = 5)
            csw_owners[owner_cards]['entry'] = cards_entry

            choose_cards_button = tkinter.Button(frame, image = img_cards)
            choose_cards_button.image = img_cards  # Keep a reference
            choose_cards_button.grid(row = 0, column = 2, padx = 5, pady = 5)
            choose_cards_button.config(command = lambda owner_cards = owner_cards, 
                cards_entry = cards_entry: csw_owners[owner_cards]['toplevel'].show())

            clear_button = tkinter.Button(frame, image = img_clear)
            clear_button.image = img_clear  # keep a reference
            clear_button.grid(row = 0, column = 3)

    def show(self):
        self.root.mainloop()

    def fill_cards_entry(self, cards_text, owner_cards):
        csw_owners[owner_cards]['entry'].delete(0, 'end')
        csw_owners[owner_cards]['entry'].insert(0, cards_text)


class CardSelectionWindow:
    def __init__(self, owner_cards):
        self.owner = owner_cards

        self.wcs = tkinter.Toplevel()
        self.wcs.title(f'Seleção de cartas - {self.owner.capitalize()}')
        self.wcs.wm_resizable(False, False)
        self.wcs.withdraw() # start hidden
        self.wcs.protocol("WM_DELETE_WINDOW", lambda: self.cancel_button_click())

        self.selected_cards = []
        self.cards_dict = {}
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
                card_button = Cards(self.owner, card_button_name, card_button_color, cards_frame, 
                    row, col).create_card_button()
                self.cards_dict[card_button_name] = card_button
        

        self.ok_button = tkinter.Button(main_frame, text = 'OK', width = 6, state = 'disabled')
        self.ok_button.config(command = lambda: self.ok_button_click())
        self.ok_button.grid(row = 1, column = 0, pady = (5, 10))

        cancel_button = tkinter.Button(main_frame, text = 'Cancel', width = 6)
        cancel_button.grid(row = 1, column = 1, pady = (5, 10))     

    def block_used_cards(self):
        blocked_cards = []
        for ow in csw_owners:
            if ow != self.owner: # all owners except the current one
                for card in csw_owners[ow]['toplevel'].selected_cards:
                    blocked_cards.append(card)
        
        for card in self.cards_dict:
            if card in blocked_cards:
                self.cards_dict[card]['state'] = 'disabled'
            elif self.cards_dict[card]['state'] == 'disabled':
                self.cards_dict[card]['state'] = 'normal'
        
    def show(self):
        self.block_used_cards()
        self.wcs.deiconify()
        
    def get_len_cards(self):
        return len(self.selected_cards)

    def activate_ok_button(self):
        self.ok_button['state'] = 'active'

    def disable_ok_button(self):
        self.ok_button['state'] = 'disabled'
    
    def ok_button_click(self):
        cards_text = ''
        for c in csw_owners[self.owner]['toplevel'].selected_cards:
            cards_text += c
        app.fill_cards_entry(cards_text, self.owner)
        self.wcs.withdraw()

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
        self.create_layout()

    def create_layout(self):
        main_frame = tkinter.Frame(self.rsw)
        main_frame.grid()

        hands_frame = tkinter.Frame(main_frame)
        hands_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        hands_index = 0
        for row in range (13):
            for col in range (13):
                hand_name = hands[hands_index]
                original_hand_color = '#FFE7B5' if 's' in hand_name \
                else '#E7EFF7' if 'o' in hand_name else '#CFDFC7'

                Hands(self.slot_name, hand_name, original_hand_color, 
                hands_frame, row, col).create_hand_button()
                hands_index += 1
        
        auxiliary_frame = tkinter.Frame(main_frame)
        auxiliary_frame.grid(row = 0, column = 2, padx = (0, 10), pady = (10, 0), sticky = 'n')

        for key, value in default_color_buttons.items():
            color_button = tkinter.Button(auxiliary_frame, 
                width = 4, text = key, bg = value['color'])
            color_button.config(command = lambda color_button = color_button
                :self.color_button_clicked(color_button))
            color_button_control[self.slot_name]['buttons'].append(color_button)
            color_button.grid(pady = 2)

        button_clear = tkinter.Button(auxiliary_frame, text = 'Clear')
        button_clear.grid(pady = 5)

        next_slot_button = tkinter.Button(auxiliary_frame, text = 'Next Slot')
        next_slot_button.grid(pady = (10, 5))

        if self.slot_name in ('pf2', 'f2', 'f3', 't2', 't3'):
            next_street_button = tkinter.Button(auxiliary_frame, text = 'Next Street')
            next_street_button.grid()

    def show(self):
        self.rsw.deiconify()

    def cancel_button_click(self):
        self.rsw.withdraw()

    def color_button_clicked(self, color_button):
        if color_button['relief'] == 'raised':
            color_button['relief'] = 'sunken'
            # updates the variable that controls the current color
            color_button_control[self.slot_name]['color'] = color_button['bg']
            
            # disable others color buttons
            for cb in color_button_control[self.slot_name]['buttons']:
                if cb != color_button:
                    cb['relief'] = 'raised'

        elif color_button['relief'] == 'sunken':
            color_button['relief'] = 'raised'
            color_button_control[self.slot_name]['color'] = ''


class Cards:
    def __init__(self, owner_cards, card_name, card_color, frame, row, column):
        self.owner = owner_cards
        self.card_name = card_name
        self.card_color = card_color
        self.frame = frame
        self.row = row
        self.column = column

    def create_card_button(self):
        card_button = tkinter.Button(self.frame, width = 2, heigh = 2, 
            text = self.card_name, fg = self.card_color)
        card_button.config(command = lambda: self.card_button_click(card_button))
        card_button.grid(row = self.row, column = self.column)
        return card_button
    
    def card_button_click(self, card_button):
        self.card_window = csw_owners[self.owner]['toplevel'] # card selection window
        qtd = self.card_window.get_len_cards()

        if card_button['bg'] == 'SystemButtonFace':
            if self.owner == 'hero' and qtd < 2:
                self.select_card(card_button)
            elif self.owner == 'flop' and qtd < 3:
                self.select_card(card_button)
            elif (self.owner == 'turn' or self.owner == 'river') and qtd == 0:
                self.select_card(card_button)
        else:
            self.deselect_card(card_button)

    def select_card(self, card_button):
        card_button['bg'] = 'gray'
        self.card_window.selected_cards.append(self.card_name)

        qtd = self.card_window.get_len_cards()

        if self.owner == 'hero' and qtd == 2:
            self.card_window.activate_ok_button()
        elif self.owner == 'flop' and qtd == 3:
            self.card_window.activate_ok_button()
        elif (self.owner == 'turn' or self.owner == 'river') and qtd == 1:
            self.card_window.activate_ok_button()

    def deselect_card(self, card_button):
        card_button['bg'] = 'SystemButtonFace'
        self.card_window.selected_cards.remove(self.card_name)

        qtd = self.card_window.get_len_cards()

        if self.owner == 'hero' and qtd < 2:
            self.card_window.disable_ok_button()
        elif self.owner == 'flop' and qtd < 3:
            self.card_window.disable_ok_button()
        elif (self.owner == 'turn' or self.owner == 'river') and qtd < 1:
            self.card_window.disable_ok_button()


class Hands:
    def __init__(self, slot_name, hand_name, original_hand_color, frame, row, column):
        self.slot_name = slot_name
        self.hand_name = hand_name
        self.original_hand_color = original_hand_color
        self.frame = frame
        self.row = row
        self.column = column

    def create_hand_button(self):
        hand_button = tkinter.Button(self.frame, width = 5, bg = self.original_hand_color, 
            text = self.hand_name)
        hand_button.config(command = lambda: self.hand_button_clicked(hand_button))
        hand_button.grid(row = self.row, column = self.column)

    def hand_button_clicked(self, hand_button):
        current_color = color_button_control[self.slot_name]['color']

        if current_color == '' or hand_button['bg'] == current_color:
            self.deselect_hand(hand_button)
        else:
            self.select_hand(hand_button, current_color)
    
    def select_hand(self, hand_button, current_color):
        hand_button['bg'] = current_color

    def deselect_hand(self, hand_button):
        hand_button['bg'] = self.original_hand_color


'''----------------------------------------------------------------------------------------------- '''
app = PokerRangeAnalysis()

# add topleves to the dicionary created earlier (module.py)
csw_owners['hero']['toplevel'] = CardSelectionWindow('hero')
csw_owners['flop']['toplevel'] = CardSelectionWindow('flop')
csw_owners['turn']['toplevel'] = CardSelectionWindow('turn')
csw_owners['river']['toplevel'] = CardSelectionWindow('river')

# creates the range selection window for each street
rsw_slots = {'pf1': RangeSelectionWindow('pf1'), 'pf2': RangeSelectionWindow('pf2'), 
    'f1': RangeSelectionWindow('f1'),'f2': RangeSelectionWindow('f2'),'f3': RangeSelectionWindow('f3'),
    't1': RangeSelectionWindow('t1'), 't2': RangeSelectionWindow('t2'), 't3': RangeSelectionWindow('t3'), 
    'r1': RangeSelectionWindow('r1'), 'r2': RangeSelectionWindow('r2'), 'r3': RangeSelectionWindow('r3')}

csw_owners['hero']['toplevel'].selected_cards

pf1_selected_color = ''


if __name__ == '__main__':
    app.show()
