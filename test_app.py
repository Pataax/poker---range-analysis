import tkinter, pytest
from tkinter import Tk

from app import PokerRangeAnalysis, WindowCardSelection


root = tkinter.Tk()
root.wm_resizable(False, False)
pk = PokerRangeAnalysis(root)

button_test = tkinter.Button(root)

wcs = WindowCardSelection('owner_cards', button_test, 'entry')


# layout
def test_layout_creation():
    assert pk.__init__(root) == None

def test_cards_list_amount():
    assert len(pk.creates_poker_cards()) == 169

def test_cards_combinations_amount():
    count = 0
    for hand in pk.creates_poker_cards_combinations():
        count += len(pk.creates_poker_cards_combinations()[hand])
    
    assert count == 1326

# # window card selection
# def test_gui_creation_window_card_selection():
#     assert wcs.create_gui('owner_cards') == 'tkinter.Toplevel()'

# def test_create_cards_combinations():
#     pass