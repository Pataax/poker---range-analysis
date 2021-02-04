import tkinter, pytest
from tkinter import Tk

from pprint import pprint
from app import PokerRangeAnalysis, WindowCardSelection



# layout
def test_main_layout_creation():
    global pk
    root = tkinter.Tk()
    root.wm_resizable(False, False)
    pk = PokerRangeAnalysis(root)

def test_gui_creation_window_card_selection():
    global wcs
    button_test = tkinter.Button()
    entry_test = tkinter.Entry()
    wcs = WindowCardSelection('Hero', button_test, entry_test)


# window card selection
def test_hands_list_empty():
    assert pk.creates_global_variables_lists_dicts()['hands'] == []

def test_cards_list_amount():
    assert len(pk.creates_poker_cards()) == 169

def test_cards_combinations_amount():
    count = 0
    for hand in pk.creates_poker_cards_combinations():
        count += len(pk.creates_poker_cards_combinations()[hand])
    
    assert count == 1326

def test_card_buttons_amount():
    assert len(wcs.create_gui('hero')) == 52 

def test_card_buttons_sample():
    assert '2h', '7c' in wcs.create_gui('hero')

# def test_selected_card_add_any_card():
#     assert wcs.selected_card('Hero', '') == []

# def test_selected_card_add_one_card():
#     assert wcs.selected_card('Hero', 'Ad', ) == ['Ad']

# def test_selected_card_add_two_cards():
#     assert wcs.selected_card('Hero', '7h2d', ) == ['7h', '2d']

# def test_re_add_combos():
#     pass

# def test_check_entry_filled():
#     assert wcs.check_entry_filled('Hero', '') == []

# def test_card_button_click():
#     assert wcs.card_button_click('hero', 'As')