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

# manter os testes nesta ordem, qualquer alteração irá resultar em erros
def test_card_buttons_sample():
    assert '2h', '7c' in wcs.create_gui('hero')

def test_manages_cards_add_one_card():
    assert wcs.manages_cards('Hero', 'Ks') == ['Ks']

def test_manages_cards_del_one_card():
    assert wcs.manages_cards('Hero', '', del_card ='Ks') == []

def test_manages_cards_add_two_cards():
    assert wcs.manages_cards('Hero', 'KsKd') == ['Ks', 'Kd']

def test_manages_cards_del_two_cards():
    assert wcs.manages_cards('Hero', '', del_card ='KsKd') == []

def test_removes_combos_amount_hands():
    foo, bar = wcs.removes_combos('ks')
    assert len(foo) == 25

def test_removes_combos_one_card():
    foo, bar = wcs.removes_combos('Qs') #dict
    for hand in foo:
        for combo in foo[hand]:
            assert 'Qs' in combo

    for hand in bar:
        for combo in bar[hand]:
            assert 'Qs' not in combo

def re_add_combos_one_card():
    foo = wcs.re_add_combos('Qs', 'Hero')
    for hand in foo:
        for combo in foo[hand]:
            assert 'Qs' not in combo
