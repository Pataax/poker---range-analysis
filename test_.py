"""Unit Tests"""

import pytest
import tkinter
from app import app, csw_owners, rsw_slots, Hands, Cards


@pytest.fixture()
def new_app():
    return app

@pytest.fixture()
def csw_hero():
    return csw_owners['hero']

@pytest.fixture()
def csw_flop():
    return csw_owners['flop']

@pytest.fixture()
def csw_turn():
    return csw_owners['turn']

@pytest.fixture()
def csw_river():
    return csw_owners['river']

@pytest.fixture()
def pf1_rsw():
    return rsw_slots['pf1']

@pytest.fixture()
def pf2_rsw():
    return rsw_slots['pf2']

@pytest.fixture()
def f1_rsw():
    return rsw_slots['f1']

@pytest.fixture()
def f2_rsw():
    return rsw_slots['f2']

@pytest.fixture()
def f3_rsw():
    return rsw_slots['f3']

@pytest.fixture()
def t1_rsw():
    return rsw_slots['t1']

@pytest.fixture()
def t2_rsw():
    return rsw_slots['t2']

@pytest.fixture()
def t3_rsw():
    return rsw_slots['t3']

@pytest.fixture()
def r1_rsw():
    return rsw_slots['r1']

@pytest.fixture()
def r2_rsw():
    return rsw_slots['r2']

@pytest.fixture()
def r3_rsw():
    return rsw_slots['r3']


class TestAppInitialParameters:
    def test_widgets_dict_keys(self, new_app):
        assert list(new_app.widgets.keys()) == ['pf1', 'pf2', 'f1', 'f2', 'f3', 
        't1', 't2', 't3', 'r1', 'r2', 'r3', 'hero', 'flop', 'turn', 'river',]

    def test_widgets_dict_hero_entries_stores_entries_type(self, new_app):
        assert type(new_app.widgets['hero']['entries']) == type(tkinter.Entry())

    def test_widgets_dict_flop_choose_button_stores_button_type(self, new_app):
        assert type(new_app.widgets['flop']['choose_button']) == type(tkinter.Button())


class TestAppButtons:
    def test_river_choose_button_works(self, new_app):
        assert new_app.widgets['river']['choose_button'].invoke() == \
            'the card selection window was displayed'

    def test_turn_clear_button_works(self, new_app):
        assert new_app.widgets['turn']['clear_button'].invoke()

    def test_pf1_button_works(self, new_app):
        assert new_app.widgets['pf1'].invoke() == 'the range selection window was displayed'

    def test_fill_cards_entry_function(self, new_app):
        assert new_app.fill_cards_entry('hero', 'AxAx') == 'AxAx'


class TestCardSelectionWindowInitialParameter:
    def test_selected_cards_dict_starts_empty(self, csw_hero):
        assert csw_hero.selected_cards == []

    def test_card_dict_starts_52_cards(self, csw_hero):
        assert len(csw_hero.card_dict) == 52

    def test_card_dict_stores_instances(self, csw_hero):
        assert isinstance(csw_hero.card_dict['2c'], Cards) == True

    def test_ok_button_starts_disabled(self, csw_hero):
        assert csw_hero.ok_button['state'] == 'disabled'

    def test_ok_button_can_be_clicked(self, csw_hero):
        assert csw_hero.ok_button.invoke() == ''


class TestCards:
    def test_card_background_start_as_systembuttonface(self, csw_hero):
        assert csw_hero.card_dict['Th'].button['bg'] == 'SystemButtonFace'
    
    def test_card_select_append_card_to_list(self, csw_hero):
        assert csw_hero.card_dict['Th'].button.invoke()[0][0] == 'Th'

    def test_card_select_change_card_background_to_gray(self, csw_hero):
        assert csw_hero.card_dict['Th'].button['bg'] == 'gray'

    def test_card_deselect_remove_card_to_list(self, csw_hero):
        assert csw_hero.card_dict['Th'].button.invoke()[0] == ''

    def test_deselect_card_change_card_background_to_systembuttonface_again(self, csw_hero):
        assert csw_hero.card_dict['Th'].button['bg'] == 'SystemButtonFace'


class TestCardSelectionWindowOkandClearButtons:
    def test_select_just_1_card_on_hero_not_activate_ok_button(self, csw_hero):
        assert csw_hero.card_dict['Qs'].card_button_click()[1] == 'disabled'

    def test_select_second_card_on_hero_activate_ok_button(self, csw_hero):
        assert csw_hero.card_dict['Ks'].card_button_click()[1] == 'active'

    def test_ok_button_click(self, csw_hero):
        assert csw_hero.ok_button_click() == 'QsKs'

    def test_deselect_1_of_2_card_on_hero_disable_ok_button(self, csw_hero):
        assert csw_hero.card_dict['Qs'].card_button_click()[1] == 'disabled'

    def test_deselect_second_card_on_hero_keeps_disabled_ok_button(self, csw_hero):
        assert csw_hero.card_dict['Ks'].card_button_click()[1] == 'disabled'

    def test_flop_clear_button_clears_entry(self, new_app, csw_flop):
        csw_flop.card_dict['7c'].card_button_click()
        csw_flop.card_dict['2h'].card_button_click()
        csw_flop.card_dict['3d'].card_button_click()
        csw_flop.ok_button_click()
        assert new_app.clear_button_click('flop')[0] == ''

    def test_flop_clear_button_clears_selected_list(self, new_app):
        assert new_app.clear_button_click('flop')[1] == []


class TestCardSelectionSelectingCards:
    def test_hero_selected_cards_are_disabled_in_remaining_cardselecwindows(self,
    csw_hero, csw_flop, csw_turn, csw_river):
        csw_hero.card_dict['Ad'].button.invoke()
        csw_hero.card_dict['Kd'].button.invoke()
        csw_hero.ok_button.invoke()

        csw_flop.show()
        assert csw_flop.card_dict['Ad'].button['state'] == 'disabled'
        assert csw_flop.card_dict['Kd'].button['state'] == 'disabled'

        csw_turn.show()
        assert csw_turn.card_dict['Ad'].button['state'] == 'disabled'
        assert csw_turn.card_dict['Kd'].button['state'] == 'disabled'

        csw_river.show()
        assert csw_river.card_dict['Ad'].button['state'] == 'disabled'
        assert csw_river.card_dict['Kd'].button['state'] == 'disabled'

    def test_hero_selected_card_cant_be_invoked_on_other_window(self,
    csw_flop, csw_turn, csw_river):
        assert csw_flop.card_dict['Ad'].button.invoke() == ''
        assert csw_flop.card_dict['Kd'].button.invoke() == ''
        assert csw_turn.card_dict['Ad'].button.invoke() == ''
        assert csw_turn.card_dict['Kd'].button.invoke() == ''
        assert csw_river.card_dict['Ad'].button.invoke() == ''
        assert csw_river.card_dict['Kd'].button.invoke() == ''
    
    def test_hero_selected_card_cant_be_clicked_on_other_window(self,
    csw_flop, csw_turn, csw_river):
        assert csw_turn.card_dict['Ad'].card_button_click() == "button can't be clicked"
        assert csw_turn.card_dict['Kd'].card_button_click() == "button can't be clicked"
        assert csw_flop.card_dict['Ad'].card_button_click() == "button can't be clicked"
        assert csw_flop.card_dict['Kd'].card_button_click() == "button can't be clicked"
        assert csw_river.card_dict['Ad'].card_button_click() == "button can't be clicked"
        assert csw_river.card_dict['Kd'].card_button_click() == "button can't be clicked"

    def test_flop_selected_cards_are_disabled_in_remaining_cardselecwindows(self,
    csw_hero, csw_flop, csw_turn, csw_river):
        csw_flop.card_dict['Ah'].card_button_click()
        csw_flop.card_dict['Kh'].card_button_click()
        csw_flop.card_dict['Qh'].card_button_click()
        csw_flop.ok_button.invoke()

        csw_hero.show()
        assert csw_hero.card_dict['Ah'].button['state'] == 'disabled'
        assert csw_hero.card_dict['Kh'].button['state'] == 'disabled'
        assert csw_hero.card_dict['Qh'].button['state'] == 'disabled'

        csw_turn.show()
        assert csw_turn.card_dict['Ah'].button['state'] == 'disabled'
        assert csw_turn.card_dict['Kh'].button['state'] == 'disabled'
        assert csw_turn.card_dict['Qh'].button['state'] == 'disabled'

        csw_river.show()
        assert csw_river.card_dict['Ah'].button['state'] == 'disabled'
        assert csw_river.card_dict['Kh'].button['state'] == 'disabled'
        assert csw_river.card_dict['Qh'].button['state'] == 'disabled'
        
    def test_flop_selected_card_cant_be_selected_on_other_window(self,
    csw_hero, csw_turn, csw_river):
        assert csw_hero.card_dict['Ah'].button.invoke() == ''
        assert csw_hero.card_dict['Kh'].button.invoke() == ''
        assert csw_turn.card_dict['Ah'].button.invoke() == ''
        assert csw_turn.card_dict['Kh'].button.invoke() == ''
        assert csw_river.card_dict['Ah'].button.invoke() == ''
        assert csw_river.card_dict['Kh'].button.invoke() == ''

    def test_turn_selected_cards_are_disabled_in_remaining_cardselecwindows(self,
    csw_hero, csw_flop, csw_turn, csw_river):
        csw_turn.card_dict['As'].card_button_click()
        csw_turn.ok_button.invoke()

        csw_hero.show()
        assert csw_hero.card_dict['As'].button['state'] == 'disabled'

        csw_flop.show()
        assert csw_flop.card_dict['As'].button['state'] == 'disabled'

        csw_river.show()
        assert csw_river.card_dict['As'].button['state'] == 'disabled'

    def test_turn_selected_card_cant_be_selected_on_other_window(self,
    csw_hero, csw_flop, csw_river):
        assert csw_hero.card_dict['As'].button.invoke() == ''
        assert csw_flop.card_dict['As'].button.invoke() == ''
        assert csw_river.card_dict['As'].button.invoke() == ''

    def test_river_selected_cards_are_disabled_in_remaining_cardselecwindows(self,
    csw_hero, csw_flop, csw_turn, csw_river):
        csw_river.card_dict['Ac'].card_button_click()
        csw_river.ok_button.invoke()

        csw_hero.show()
        assert csw_hero.card_dict['Ac'].button['state'] == 'disabled'

        csw_flop.show()
        assert csw_flop.card_dict['Ac'].button['state'] == 'disabled'

        csw_turn.show()
        assert csw_turn.card_dict['Ac'].button['state'] == 'disabled'

    def test_river_selected_card_cant_be_selected_on_other_window(self,
    csw_hero, csw_flop, csw_turn):
        assert csw_hero.card_dict['Ac'].button.invoke() == ''
        assert csw_flop.card_dict['Ac'].button.invoke() == ''
        assert csw_turn.card_dict['Ac'].button.invoke() == ''


class TestRangeSelection:
    def test_hands_dict_starts_169_hands(self, pf1_rsw):
        assert len(pf1_rsw.hands_dict) == 169

    def test_hands_dict_store_hands_instance(self, pf1_rsw):
        assert isinstance(pf1_rsw.hands_dict['AA'], Hands) == True

    def test_color_buttons_dict_len_is_equal_8(self, pf1_rsw):
        assert len(pf1_rsw.color_buttons) == 8

    def test_color_buttons_dict_stores_buttons(self, pf1_rsw):
        assert type(pf1_rsw.color_buttons['2']) == type(tkinter.Button())

    def test_select_a_color_button_returns_sunken_relief(self, pf1_rsw):
        assert pf1_rsw.color_buttons['1'].invoke()[0] == 'sunken'

    def test_select_a_color_button_returns_current_color(self, pf1_rsw):
        assert pf1_rsw.current_color == '#B2301E'

    def test_select_a_color_button_deselect_all_others(self, pf1_rsw):
        for cb in pf1_rsw.color_buttons:
            if cb != '1':
                assert pf1_rsw.color_buttons[cb]['relief'] == 'raised'

    def test_select_other_color_button_deselect_the_first(self, pf1_rsw):
        pf1_rsw.color_buttons['2'].invoke()
        assert pf1_rsw.color_buttons['1']['relief'] == 'raised'

    def test_deselect_color_button_returns_current_color_equal_empty(self, pf1_rsw):
        pf1_rsw.color_buttons['2'].invoke()
        assert pf1_rsw.current_color == ''

    def test_deselect_color_button_return_raised_relief(self, pf1_rsw):
        assert pf1_rsw.color_buttons['2']['relief'] == 'raised'

    def test_some_slots_have_next_street_button(self, pf2_rsw, f2_rsw, f3_rsw, t2_rsw, t3_rsw):
        assert pf2_rsw.widgets['next_street'] != ''
        assert f2_rsw.widgets['next_street'] != ''
        assert f3_rsw.widgets['next_street'] != ''
        assert t2_rsw.widgets['next_street'] != ''
        assert t3_rsw.widgets['next_street'] != ''

    def test_some_slots_doesnt_have_next_street_button(self, pf1_rsw, f1_rsw, t1_rsw):
        assert 'next_street' not in pf1_rsw.widgets
        assert 'next_street' not in f1_rsw.widgets
        assert 'next_street' not in t1_rsw.widgets


class TestHands:
    def test_selfbutton_store_a_button(self, pf1_rsw):
        assert type(pf1_rsw.hands_dict['98o'].button) == type(tkinter.Button())

    def test_pairs_hands_have_6_combos(self, pf1_rsw):
        for hand in pf1_rsw.hands_dict:
            if hand[0] == hand[1]:
                assert pf1_rsw.hands_dict[hand].hand_combos == 6

    def test_suited_hands_have_4_combos(self, pf1_rsw):
        for hand in pf1_rsw.hands_dict:
            if 's' in hand:
                assert pf1_rsw.hands_dict[hand].hand_combos == 4

    def test_offsuited_hands_have_12_combos(self, pf1_rsw):
        for hand in pf1_rsw.hands_dict:
            if 'o' in hand:
                assert pf1_rsw.hands_dict[hand].hand_combos == 12

    def test_select_hand_without_first_selecting_color_returns_deselected_hand(self, pf1_rsw):
        assert pf1_rsw.hands_dict['JTo'].button.invoke()[0] == 'the hand has been deselected'

    def test_select_hand_without_first_selecting_color_returns_button_with_original_color(self, pf1_rsw):
        assert pf1_rsw.hands_dict['JTo'].button['bg'] == pf1_rsw.hands_dict['JTo'].original_hand_color

    def test_selec_hand_with_current_color_returns_selected_hand(self, pf1_rsw):
        pf1_rsw.color_buttons['1'].invoke()
        assert pf1_rsw.hands_dict['QQ'].button.invoke()[0] == 'the hand has been selected'

    def test_select_hand_with_current_color_returns_colorful_button(self, pf1_rsw):
        assert pf1_rsw.hands_dict['QQ'].button['bg'] == '#B2301E'

    def test_select_hand_with_current_color_return_selectec_combos(self, pf1_rsw):
        assert pf1_rsw.selected_combos == 6


if __name__ == '__main__':
    pytest.main()
