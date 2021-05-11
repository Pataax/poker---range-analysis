"""Unit Tests"""

import pytest
import tkinter
from app import PokerRangeAnalysis, CardSelectionWindow, Cards



@pytest.fixture(scope = 'module')
def app():
    return PokerRangeAnalysis()

@pytest.fixture(scope = 'module')
def hero_csw():
    return CardSelectionWindow('hero')

@pytest.fixture(scope = 'module')
def flop_csw():
    return CardSelectionWindow('flop')

@pytest.fixture(scope = 'module')
def turn_csw():
    return CardSelectionWindow('turn')

@pytest.fixture(scope = 'module')
def river_csw():
    return CardSelectionWindow('river')


class TestAppInitialParameters:
    def test_app_widgets_dict_has_hero_flop_turn_river_as_keys(self, app):
        assert list(app.widgets.keys()) == ['hero', 'flop', 'turn', 'river']

    def test_app_card_selection_entries_dict_stores_entries_type(self, app):
        assert type(app.widgets['hero']['entries']) == type(tkinter.Entry())

    def test_app_widgets_dict_owner_card_selection_has_stores_button(self, app):
        assert type(app.widgets['flop']['choose_button']) == type(tkinter.Button())


class TestAppButtonsWorks:
    def test_app_choose_button_works(self, app):
        assert app.widgets['river']['choose_button'].invoke() == \
            'the card selection window was displayed'

    def test_app_clear_button_works(self, app):
        app.widgets['turn']['clear_button'].invoke()


class TestCardSelectionWindowInitialParameter:
    def test_selected_cards_dict_starts_empty(self, hero_csw):
        assert hero_csw.selected_cards == []

    def test_card_dict_starts_52_cards(self, hero_csw):
        assert len(hero_csw.card_dict) == 52

    def test_card_dict_stores_instances(self, hero_csw):
        any_frame = tkinter.Frame()
        any_card_instance = Cards('bruno', 'Ax', 'green', any_frame, 0, 0)
        assert type(hero_csw.card_dict['2c']) == type(any_card_instance)

    def test_ok_button_starts_disabled(self, hero_csw):
        assert hero_csw.ok_button['state'] == 'disabled'


class TestCardsFunctions:
    def test_card_select_append_card_to_list(self, hero_csw):
        assert hero_csw.card_dict['Th'].card_button_click()[0] == ['Th']

    def test_card_deselect_remove_card_to_list(self, hero_csw):
        assert hero_csw.card_dict['Th'].card_button_click()[0] == []

    def test_card_background_start_as_systembuttonface(self, hero_csw):
        assert hero_csw.card_dict['Th'].button['bg'] == 'SystemButtonFace'

    def test_card_select_change_card_background_to_gray(self, hero_csw):
        hero_csw.card_dict['Th'].card_button_click()
        assert hero_csw.card_dict['Th'].button['bg'] == 'gray'

    def test_deselect_card_change_card_background_to_systembuttonface_again(self, hero_csw):
        hero_csw.card_dict['Th'].card_button_click()
        assert hero_csw.card_dict['Th'].button['bg'] == 'SystemButtonFace'


class TestCardSelectionWindowOkButtonStatus:
    def test_select_just_1_card_on_hero_not_activate_ok_button(self, hero_csw):
        assert hero_csw.card_dict['Qs'].card_button_click()[1] == 'disabled'

    def test_select_second_card_on_hero_activate_ok_button(self, hero_csw):
        assert hero_csw.card_dict['Ks'].card_button_click()[1] == 'active'

    def test_fill_cards_entry_function(self, app):
        assert app.fill_cards_entry('hero', 'AxAx') == 'AxAx'

    def test_ok_button_click(self, hero_csw):
        assert hero_csw.ok_button_click() == 'QsKs'

    def test_deselect_1_of_2_card_on_hero_disable_ok_button(self, hero_csw):
        assert hero_csw.card_dict['Qs'].card_button_click()[1] == 'disabled'

    def test_deselect_second_card_on_hero_keeps_disabled_ok_button(self, hero_csw):
        assert hero_csw.card_dict['Ks'].card_button_click()[1] == 'disabled'


class TestCardSelectionWindowClearButton:
    def test_flop_clear_button_clears_entry_and_list(self, app, flop_csw):
        flop_csw.card_dict['7c'].card_button_click()
        flop_csw.card_dict['2h'].card_button_click()
        flop_csw.card_dict['3d'].card_button_click()
        flop_csw.ok_button_click()
        assert app.clear_button_click('flop')[0] == ''
        assert app.clear_button_click('flop')[1] == []

        
class TestCardSelectionSelectingCards:
    def test_hero_selected_cards_are_disabled_in_remaining_cardselecwindows(self,
    hero_csw, flop_csw, turn_csw, river_csw):
        hero_csw.card_dict['Ad'].card_button_click()
        hero_csw.card_dict['Kd'].card_button_click()
        flop_csw.show()
        assert flop_csw.card_dict['Ad'].button['state'] == 'disabled'
        turn_csw.show()
        assert turn_csw.card_dict['Ad'].button['state'] == 'disabled'
        river_csw.show()
        assert river_csw.card_dict['Ad'].button['state'] == 'disabled'

    def test_hero_selected_card_cant_be_selected_on_other_window(self,
    flop_csw, turn_csw, river_csw):
        assert turn_csw.card_dict['Ad'].card_button_click() == "button can't be clicked"
        assert turn_csw.card_dict['Kd'].card_button_click() == "button can't be clicked"
        assert flop_csw.card_dict['Ad'].card_button_click() == "button can't be clicked"
        assert flop_csw.card_dict['Kd'].card_button_click() == "button can't be clicked"
        assert river_csw.card_dict['Ad'].card_button_click() == "button can't be clicked"
        assert river_csw.card_dict['Kd'].card_button_click() == "button can't be clicked"

    def test_flop_selected_cards_are_disabled_in_remaining_cardselecwindows(self,
    hero_csw, flop_csw, turn_csw, river_csw):
        flop_csw.card_dict['Ah'].card_button_click()
        flop_csw.card_dict['Kh'].card_button_click()
        flop_csw.card_dict['Qh'].card_button_click()
        hero_csw.show()
        assert hero_csw.card_dict['Ah'].button['state'] == 'disabled'
        turn_csw.show()
        assert turn_csw.card_dict['Ah'].button['state'] == 'disabled'
        river_csw.show()
        assert river_csw.card_dict['Ah'].button['state'] == 'disabled'

    def test_flop_selected_card_cant_be_selected_on_other_window(self,
    hero_csw, turn_csw, river_csw):
        assert turn_csw.card_dict['Ah'].card_button_click() == "button can't be clicked"
        assert turn_csw.card_dict['Kh'].card_button_click() == "button can't be clicked"
        assert hero_csw.card_dict['Ah'].card_button_click() == "button can't be clicked"
        assert hero_csw.card_dict['Kh'].card_button_click() == "button can't be clicked"
        assert river_csw.card_dict['Ah'].card_button_click() == "button can't be clicked"
        assert river_csw.card_dict['Kh'].card_button_click() == "button can't be clicked"


if __name__ == '__main__':
    pytest.main()
