"""Unit Tests"""

import pytest
import tkinter
from app import Hands, PokerRangeAnalysis, CardSelectionWindow, RangeSelectionWindow, Cards



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

@pytest.fixture(scope = 'module')
def pf1_rsw():
    return RangeSelectionWindow('pf1')


class TestAppInitialParameters:
    def test_app_widgets_dict_keys(self, app):
        assert list(app.widgets.keys()) == ['pf1', 'pf2', 'f1', 'f2', 'f3', 
        't1', 't2', 't3', 'r1', 'r2', 'r3', 'hero', 'flop', 'turn', 'river',]

    def test_app_card_selection_entries_dict_stores_entries_type(self, app):
        assert type(app.widgets['hero']['entries']) == type(tkinter.Entry())

    def test_app_widgets_dict_owner_card_selection_has_stores_button(self, app):
        assert type(app.widgets['flop']['choose_button']) == type(tkinter.Button())


class TestAppButtonsWorks:
    def test_app_choose_button_works(self, app):
        assert app.widgets['river']['choose_button'].invoke() == \
            'the card selection window was displayed'

    def test_app_clear_button_works(self, app):
        assert app.clear_button_click('turn')

    def test_app_pf1_button_works(self, app):
        assert app.widgets['pf1'].invoke() == 'the range selection window was displayed'


class TestCardSelectionWindowInitialParameter:
    def test_selected_cards_dict_starts_empty(self, hero_csw):
        assert hero_csw.selected_cards == []

    def test_card_dict_starts_52_cards(self, hero_csw):
        assert len(hero_csw.card_dict) == 52

    def test_card_dict_stores_instances(self, hero_csw):
        assert isinstance(hero_csw.card_dict['2c'], Cards) == True

    def test_ok_button_starts_disabled(self, hero_csw):
        assert hero_csw.ok_button['state'] == 'disabled'


class TestCards:
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


class TestRangeSelection:
    def test_hands_dict_starts_169_hands(self, pf1_rsw):
        assert len(pf1_rsw.hands_dict) == 169

    def test_hands_dict_store_hands_instance(self, pf1_rsw):
        assert isinstance(pf1_rsw.hands_dict['AA'], Hands) == True

    def test_color_buttons_dict_len_is_equal_8(self, pf1_rsw):
        assert len(pf1_rsw.color_buttons) == 8

    def test_color_buttons_stores_buttons(self, pf1_rsw):
        assert type(pf1_rsw.color_buttons['2']) == type(tkinter.Button())

    def test_select_a_color_button_returns_sunken_relief(self, pf1_rsw):
        assert pf1_rsw.color_buttons['1'].invoke() == 'sunken'

    def test_select_a_color_button_returns_current_color(self, pf1_rsw):
        assert pf1_rsw.current_color == '#B2301E'

    def test_select_a_color_button_deselect_all_others(self, pf1_rsw):
        assert pf1_rsw.deselect_other_color_buttons('1') == 'all other color buttons have been deselected'

    def test_select_other_color_button_deselect_the_first(self, pf1_rsw):
        pf1_rsw.color_buttons['2'].invoke()
        assert pf1_rsw.color_buttons['1']['relief'] == 'raised'

    def test_deselect_color_button_returns_current_color_equal_empty(self, pf1_rsw):
        pf1_rsw.color_buttons['2'].invoke()
        assert pf1_rsw.current_color == ''


class TestHands:
    def test_selfbutton_store_a_button(self, pf1_rsw):
        assert type(pf1_rsw.hands_dict['98o'].button) == type(tkinter.Button())

    # def test_select_hand_without__first_selecting_color_returns_nothing(self, pf1_rsw):
    #     assert pf1_rsw.hands_dict['JTo'].button.invoke() == 'a carta foi deselecionada'

    # def test_selec_hand_with_current_color_return_colorful_button(self, pf1_rsw):
    #     pf1_rsw.color_buttons['3'].invoke()
    #     assert pf1_rsw.hands_dict['QQ'].hand_button_clicked() == 'a carta foi selecionada'


if __name__ == '__main__':
    pytest.main()
