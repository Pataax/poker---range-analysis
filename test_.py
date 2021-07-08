from tkinter.constants import S
import pytest
import tkinter
from app import app, csw_owners, rsw_slots, Hands, Cards


@pytest.fixture()
def new_app():
    return app

@pytest.fixture()
def all_csw():
    return {'hero': csw_owners['hero'], 'flop': csw_owners['flop'], 
            'turn': csw_owners['turn'], 'river': csw_owners['river']}

@pytest.fixture()
def all_rsw():
    return {'pf1': rsw_slots['pf1'], 'pf2': rsw_slots['pf2'], 
            'f1': rsw_slots['f1'], 'f2': rsw_slots['f2'], 'f3': rsw_slots['f3'],
            't1': rsw_slots['t1'], 't2': rsw_slots['t2'], 't3': rsw_slots['t3'], 
            'r1': rsw_slots['r1'], 'r2': rsw_slots['r2'], 'r3': rsw_slots['r3']}

streets_name = ['hero', 'flop', 'turn', 'river']
slots_name = ('pf1', 'pf2', 'f1', 'f2', 'f3', 't1', 't2', 't3', 'r1', 'r2', 'r3')


# @pytest.mark.isolate
class TestAppInitialParameters:
    def test_widgets_dict_keys(self, new_app):
        assert list(new_app.widgets.keys()) == ['pf1', 'pf2', 'f1', 'f2', 'f3', 
        't1', 't2', 't3', 'r1', 'r2', 'r3', 'hero', 'flop', 'turn', 'river',]

    def test_widgets_dict_streets_entries_stores_entries_type(self, new_app):
        for street in streets_name:
            assert type(new_app.widgets[street]['entries']) == type(tkinter.Entry())

    def test_widgets_dict_streets_choose_buttons_stores_button_type(self, new_app):
        for street in streets_name:
            assert type(new_app.widgets[street]['choose_button']) == type(tkinter.Button())


# @pytest.mark.isolate
class TestAppButtons:
    def test_streets_choose_buttons_works(self, new_app):
        for street in streets_name:
            assert new_app.widgets[street]['choose_button'].invoke() == \
                'the card selection window was displayed'

    def test_slots_buttons_works(self, new_app, all_rsw):
        for slot in all_rsw:
            assert new_app.widgets[slot].invoke() == 'the range selection window was displayed'

    def test_fill_cards_entry_function(self, new_app):
        for street in streets_name:
            assert new_app.fill_cards_entry(street, 'AxAx') == 'AxAx'

    def test_clear_button_click_clears_entry(self, new_app):
        for street in streets_name:
            assert new_app.widgets[street]['clear_button'].invoke() == ''


# @pytest.mark.isolate
class TestCardSelectionWindowInitialParameter:
    def test_selected_cards_dict_starts_empty(self, all_csw):
        for owner in all_csw:
            assert all_csw[owner].selected_cards == []

    def test_cards_dict_starts_52_cards(self, all_csw):
        for owner in all_csw:
            assert len(all_csw[owner].cards_dict) == 52

    def test_cards_dict_stores_instances(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                assert isinstance(all_csw[owner].cards_dict[card], Cards) == True

    def test_ok_buttons_starts_disabled(self, all_csw):
        for owner in all_csw:
            assert all_csw[owner].ok_button['state'] == 'disabled'

    def test_ok_buttons_can_be_clicked(self, all_csw):
        for owner in all_csw:
            assert all_csw[owner].ok_button.invoke() == ''


# @pytest.mark.isolate
class TestCards:
    def test_cards_background_starts_as_SystemButtonFace(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                assert all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace'
    
    def test_select_card_appends_card_to_list(self, all_csw):
        for owner in all_csw:
            all_csw[owner].cards_dict['Th'].button.invoke()
            assert all_csw[owner].selected_cards == ['Th']
    
    def test_select_card_remove_hand_combos(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                for rmv_combo in all_rsw[slot].hands_dict[hand].removed_combos:
                    assert 'Th' in rmv_combo

    def test_select_card_change_card_background_to_gray(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                if card == 'Th':
                    assert all_csw[owner].cards_dict['Th'].button['bg'] == 'gray'
                else:
                    assert all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace'

    def test_deselect_card_removes_card_to_list(self, all_csw):
        for owner in all_csw:
            all_csw[owner].cards_dict['Th'].button.invoke()
            assert all_csw[owner].selected_cards == []
    
    def test_deselect_card_remove_removed_hand_combos(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                assert all_rsw[slot].hands_dict[hand].removed_combos == []

    def test_deselect_card_changes_card_background_to_systembuttonface_again(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                assert all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace'


# @pytest.mark.isolate
class TestCardSelectionWindowOkandClearButtons:
    def test_select_just_1_card_on_hero_not_activate_ok_button(self, all_csw):
        all_csw['hero'].cards_dict['Qs'].button.invoke()
        assert all_csw['hero'].ok_button['state'] == 'disabled'

    def test_select_second_card_on_hero_activate_ok_button(self, all_csw):
        all_csw['hero'].cards_dict['Ks'].button.invoke()
        assert all_csw['hero'].ok_button['state'] == 'active'

    def test_ok_button_click(self, all_csw):
        all_csw['hero'].ok_button_click()
        assert app.widgets['hero']['entries'].get() == 'QsKs'

    def test_deselect_1_of_2_card_on_hero_disable_ok_button(self, all_csw):
        all_csw['hero'].cards_dict['Qs'].button.invoke()
        assert all_csw['hero'].ok_button['state'] == 'disabled'

    def test_deselect_second_card_on_hero_keeps_disabled_ok_button(self, all_csw):
        all_csw['hero'].cards_dict['Ks'].button.invoke()
        assert all_csw['hero'].ok_button['state'] == 'disabled'

    def test_flop_clear_button_clears_entry(self, new_app, all_csw):
        all_csw['flop'].cards_dict['7c'].card_button_click()
        all_csw['flop'].cards_dict['2h'].card_button_click()
        all_csw['flop'].cards_dict['3d'].card_button_click()
        all_csw['flop'].ok_button_click()
        new_app.clear_button_click('flop')
        assert new_app.widgets['flop']['entries'].get() == ''

    def test_flop_clear_button_clears_selected_list(self, all_csw):
        assert all_csw['flop'].selected_cards == []


# @pytest.mark.isolate
class TestCardSelectionSelectingCards:
    def test_selected_cards_are_disabled_in_remaining_cardselecwindows(self, all_csw):
        for owner in all_csw:
            if owner == 'hero':
                all_csw[owner].cards_dict['Ad'].button.invoke()
                all_csw[owner].cards_dict['Kd'].button.invoke()
            if owner == 'flop':
                all_csw[owner].cards_dict['Ah'].button.invoke()
                all_csw[owner].cards_dict['Kh'].button.invoke()
                all_csw[owner].cards_dict['Qh'].button.invoke()
            if owner == 'turn':
                all_csw[owner].cards_dict['As'].button.invoke()
            if owner == 'river':
                all_csw[owner].cards_dict['Ac'].button.invoke()

        for owner in all_csw:
            all_csw[owner].show()
            for card in all_csw[owner].cards_dict:
                if card in ('Ad', 'Kd', 'Ah', 'Kh', 'Qh', 'As', 'Ac'):
                    if all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace':
                        assert all_csw[owner].cards_dict[card].button['state'] == 'disabled'

    def test_selected_card_cant_be_invoked_on_other_window(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                if card in ('Ad', 'Kd', 'Ah', 'Kh', 'Qh', 'As', 'Ac'):
                    if all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace':
                        assert all_csw[owner].cards_dict[card].button.invoke() == ''

    def test_selected_card_cant_be_clicked_on_other_window(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                if card in ('Ad', 'Kd', 'Ah', 'Kh', 'Qh', 'As', 'Ac'):
                    if all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace':
                        assert all_csw[owner].cards_dict[card].card_button_click() == \
                            "button can't be clicked"

    def test_deselected_cards_are_available_in_remaining_cardselecwindows(self, all_csw):
        for owner in all_csw:
            if owner == 'hero':
                all_csw[owner].cards_dict['Ad'].button.invoke()
                all_csw[owner].cards_dict['Kd'].button.invoke()
            if owner == 'flop':
                all_csw[owner].cards_dict['Ah'].button.invoke()
                all_csw[owner].cards_dict['Kh'].button.invoke()
                all_csw[owner].cards_dict['Qh'].button.invoke()
            if owner == 'turn':
                all_csw[owner].cards_dict['As'].button.invoke()
            if owner == 'river':
                all_csw[owner].cards_dict['Ac'].button.invoke()

        for owner in all_csw:
            all_csw[owner].show()
            for card in all_csw[owner].cards_dict:
                assert all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace'
                assert all_csw[owner].cards_dict[card].button['state'] == 'normal'


# @pytest.mark.isolate
class TestRSWInitialParameters:
    def test_hands_dict_starts_169_hands(self, all_rsw):
        for slot in all_rsw:
            assert len(all_rsw[slot].hands_dict) == 169

    def test_hands_dict_store_hands_instance(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                assert isinstance(all_rsw[slot].hands_dict[hand], Hands) == True

    def test_color_buttons_dict_len_is_equal_8(self, all_rsw):
        for slot in all_rsw:
            assert len(all_rsw[slot].color_buttons) == 8

    def test_color_buttons_dict_stores_buttons(self, all_rsw):
        for slot in all_rsw:
            for cb_name in all_rsw[slot].color_buttons:
                assert type(all_rsw[slot].color_buttons[cb_name]) == type(tkinter.Button())


# @pytest.mark.isolate
class TestRSWColorButtons:
    def test_select_a_color_button_returns_sunken_relief(self, all_rsw):
        for slot in all_rsw:
            assert all_rsw[slot].color_buttons['1'].invoke() == 'sunken'

    def test_select_a_color_button_returns_current_color(self, all_rsw):
        for slot in all_rsw:
            assert all_rsw[slot].current_color == '#B2301E'

    def test_select_a_color_button_deselect_all_others(self, all_rsw):
        for slot in all_rsw:
            for cb in all_rsw[slot].color_buttons:
                if cb != '1':
                    assert all_rsw[slot].color_buttons[cb]['relief'] == 'raised'

    def test_select_other_color_button_deselect_the_first(self, all_rsw):
        for slot in all_rsw:
            all_rsw[slot].color_buttons['2'].invoke()
            assert all_rsw[slot].color_buttons['1']['relief'] == 'raised'

    def test_deselect_color_button_returns_current_color_equal_empty(self, all_rsw):
        for slot in all_rsw:
            all_rsw[slot].color_buttons['2'].invoke()
            assert all_rsw[slot].current_color == ''

    def test_deselect_color_button_return_raised_relief(self, all_rsw):
        for slot in all_rsw:
            assert all_rsw[slot].color_buttons['2']['relief'] == 'raised'


# @pytest.mark.isolate
class TestRSWSlots:
    def test_some_slots_have_next_street_button(self, all_rsw):
        for slot in all_rsw:
            if slot in ('pf2', 'f2', 'f3', 't2', 't3'):
                assert all_rsw[slot].widgets['next_street'] != ''
            else:
                assert 'next_street' not in all_rsw[slot].widgets

    def test_next_slot_button_results(self, all_rsw):
        assert all_rsw['pf1'].next_slot_button_click() == 'pf2'
        assert all_rsw['f1'].next_slot_button_click() == 'f2'
        assert all_rsw['f2'].next_slot_button_click() == 'f3'
        assert all_rsw['t1'].next_slot_button_click() == 't2'
        assert all_rsw['t2'].next_slot_button_click() == 't3'
        assert all_rsw['r1'].next_slot_button_click() == 'r2'
        assert all_rsw['r2'].next_slot_button_click() == 'r3'

    def test_next_street_results(self, all_rsw):
        assert all_rsw['pf2'].next_street_button_click() == 'f1'
        assert all_rsw['f2'].next_street_button_click() == 't1'
        assert all_rsw['f3'].next_street_button_click() == 't1'
        assert all_rsw['t2'].next_street_button_click() == 'r1'
        assert all_rsw['t3'].next_street_button_click() == 'r1'


# @pytest.mark.isolate
class TestRSWBlockUnusedHands:
    def test_block_unused_hands(self, all_rsw):
        all_rsw['pf1'].color_buttons['1'].invoke()
        all_rsw['pf1'].hands_dict['A2s'].button.invoke()
        all_rsw['pf1'].hands_dict['A3s'].button.invoke()
        all_rsw['pf1'].hands_dict['K2s'].button.invoke()
        all_rsw['pf1'].hands_dict['K3s'].button.invoke()
        all_rsw['pf1'].color_buttons['1'].invoke()

        for hand in all_rsw['pf2'].hands_dict:
            if hand not in ['A2s', 'A3s', 'K2s', 'K3s']:
                assert all_rsw['pf2'].hands_dict[hand].button['state'] == 'disabled'
        
        all_rsw['pf1'].hands_dict['A2s'].button.invoke()
        all_rsw['pf1'].hands_dict['A3s'].button.invoke()
        all_rsw['pf1'].hands_dict['K2s'].button.invoke()
        all_rsw['pf1'].hands_dict['K3s'].button.invoke()


# @pytest.mark.isolate
class TestRSWHands:
    def test_selfbutton_store_a_button(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                assert type(all_rsw[slot].hands_dict[hand].button) == type(tkinter.Button())

    def test_card_removed_combos_start_empty(self, all_rsw):
        for slot in all_rsw:
            for card in all_rsw[slot].hands_dict:
                assert all_rsw[slot].hands_dict[card].removed_combos == []

    def test_pairs_hands_have_6_combos(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                if hand[0] == hand[1]:
                    assert all_rsw[slot].hands_dict[hand].n_hand_combos == 6

    def test_suited_hands_have_4_combos(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                if 's' in hand:
                    assert all_rsw[slot].hands_dict[hand].n_hand_combos == 4

    def test_offsuited_hands_have_12_combos(self, all_rsw):
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                if 'o' in hand:
                    assert all_rsw[slot].hands_dict[hand].n_hand_combos == 12

    def test_AKs_amount_combos(self, all_rsw):
        assert all_rsw['pf1'].hands_dict['AKs'].combos == \
            [('Ad', 'Kd'), ('Ah', 'Kh'), ('As', 'Ks'), ('Ac', 'Kc')]

    def test_ensure_no_color_selected(self, all_rsw):
        for slot in all_rsw:
            assert all_rsw[slot].current_color == ''

    def test_select_hand_pf1_without_first_selecting_color_doesnt_change_anything(self, all_rsw):
        for hand in all_rsw['pf1'].hands_dict:
            assert all_rsw['pf1'].hands_dict[hand].button.invoke() == 'nothin has been changed'

    def test_select_hand_pf1_without_first_selecting_color_keeps_button_original_color(self, all_rsw):
        for hand in all_rsw['pf1'].hands_dict:
            assert all_rsw['pf1'].hands_dict[hand].button['bg'] == \
                all_rsw['pf1'].hands_dict[hand].original_hand_color

    def test_select_hand_pf1_without_first_selecting_color_returns_selected_combos_0(self, all_rsw):
        assert all_rsw['pf1'].selected_combos == 0

    def test_select_hand_pf1_without_first_selecting_color_returns_selected_hands_empty(self, all_rsw):
        assert all_rsw['pf1'].selected_hands == []

    def test_select_hands_pf1_with_current_color_returns_colorful_button(self, all_rsw):
            all_rsw['pf1'].color_buttons['1'].invoke()
            for hand in all_rsw['pf1'].hands_dict:
                if hand in ('AA', 'AKs', 'AKo'):
                    all_rsw['pf1'].hands_dict[hand].button.invoke()
                    assert all_rsw['pf1'].hands_dict[hand].button['bg'] == '#B2301E'
                else:
                    assert all_rsw['pf1'].hands_dict[hand].button['bg'] == \
                        all_rsw['pf1'].hands_dict[hand].original_hand_color

    def test_select_hands_pf1_with_current_color_returns_selected_combos_22(self, all_rsw):
        assert all_rsw['pf1'].selected_combos == 6 + 4 + 12

    def test_select_hands_with_current_color_returns_percent_combos_1_65(self, all_rsw):
        assert all_rsw['pf1'].percent_hands_selected == ((6 + 4 + 12) / 1326) * 100  # 1.65%

    def test_select_hands_with_current_color_returns_selected_hands_list(self, all_rsw):
        assert all_rsw['pf1'].selected_hands == ['AA', 'AKs', 'AKo']

    def test_deselect_hands_pf1_returns_buttons_with_original_colors(self, all_rsw):
        all_rsw['pf1'].color_buttons['1'].invoke()
        for hand in all_rsw['pf1'].hands_dict:
            if hand in ('AA', 'AKs', 'AKo'):
                all_rsw['pf1'].hands_dict[hand].button.invoke()
            assert all_rsw['pf1'].hands_dict[hand].button['bg'] == \
                all_rsw['pf1'].hands_dict[hand].original_hand_color

    def test_deselect_hands_pf1_returns_selected_combos_0(self, all_rsw):
        assert all_rsw['pf1'].selected_combos == 0

    def test_deselect_hands_pf1_returns_percent_combos_0(self, all_rsw):
        assert all_rsw['pf1'].percent_hands_selected == 0

    def test_deselect_hands_pf1_returns_selected_hands__list_empty(self, all_rsw):
        assert all_rsw['pf1'].selected_hands == []

    def test_select_all_hands_return_percent_combos_100(self, all_rsw):
        all_rsw['pf1'].color_buttons['1'].invoke()
        for hand in all_rsw['pf1'].hands_dict:
            all_rsw['pf1'].hands_dict[hand].button.invoke()
        assert all_rsw['pf1'].percent_hands_selected == 100

    def test_select_all_hands_returns_selected_combos_1326(self, all_rsw):
        assert all_rsw['pf1'].selected_combos == 1326

    def test_select_all_hands_returns_selected_hands_list_len_169(self, all_rsw):
        assert len(all_rsw['pf1'].selected_hands) == 169

    def test_deselect_all_hands_return_percent_combos_0(self, all_rsw):
        all_rsw['pf1'].color_buttons['1'].invoke()
        all_rsw['pf1'].clear_button_click()
        assert all_rsw['pf1'].percent_hands_selected == 0

    def test_deselect_all_hands_returns_selected_combos_0(self, all_rsw):
        assert all_rsw['pf1'].selected_combos == 0

    def test_deselect_all_hands_returns_selected_hands_list_len_0(self, all_rsw):
        assert len(all_rsw['pf1'].selected_hands) == 0

    def test_reselect_hand_with_another_color_doesnt_change_selected_combo(self, all_rsw):
        all_rsw['pf1'].color_buttons['1'].invoke()
        all_rsw['pf1'].hands_dict['A2s'].button.invoke()
        assert all_rsw['pf1'].selected_combos == 4

        all_rsw['pf1'].color_buttons['2'].invoke()
        all_rsw['pf1'].hands_dict['A2s'].button.invoke()
        assert all_rsw['pf1'].selected_combos == 4
        all_rsw['pf1'].color_buttons['2'].invoke()

    def test_pf1_not_selected_hands_blocked_another_streets(self, all_rsw):
        for slot in all_rsw:
            if slot == 'pf2':
                all_rsw[slot].show()
                for hand in all_rsw[slot].hands_dict:
                    if hand not in all_rsw['pf1'].selected_hands:
                        assert all_rsw[slot].hands_dict[hand].button['state'] == 'disabled'
                    else:
                        assert all_rsw[slot].hands_dict[hand].button['state'] == 'normal'
            if slot not in ('pf1', 'pf2'):
                for hand in all_rsw[slot].hands_dict:
                    assert all_rsw[slot].hands_dict[hand].button['state'] == 'disabled'

    def test_pf2_total_combos_1326(self, all_rsw):
        # pf2 only discounts selected card blockers
        for slot in all_rsw:
            if slot == 'pf2':
                assert all_rsw[slot].total_combos == 1326
            elif slot not in ('pf1', 'pf2'):
                assert all_rsw[slot].total_combos == 0

    def test_clean_pf1_range_locks_all_hands_other_streets(self, all_rsw):
        all_rsw['pf1'].clear_button_click()
        for slot in all_rsw:
            all_rsw[slot].show()
            if slot != 'pf1':
                for hand in all_rsw[slot].hands_dict:
                    assert all_rsw[slot].hands_dict[hand].button['state'] == 'disabled'

    def test_ensure_no_card_selected(self, all_csw):
        for owner in all_csw:
            for card in all_csw[owner].cards_dict:
                assert all_csw[owner].cards_dict[card].button['bg'] == 'SystemButtonFace'

    def test_selected_card_remove_combos_except_pf1(self, all_csw, all_rsw):
        all_csw['hero'].cards_dict['Ad'].button.invoke()
        all_csw['hero'].cards_dict['Kc'].button.invoke()
        for slot in all_rsw:
            if slot == 'pf1':
                for hand in all_rsw[slot].hands_dict:   
                    assert all_rsw[slot].hands_dict[hand].removed_combos == []
            else:
                for hand in all_rsw[slot].hands_dict:
                    for combo in all_rsw[slot].hands_dict[hand].removed_combos:
                        assert ('Ad' in combo) or ('Kc' in combo)

    def test_selected_card_decreases_amount_combos(self, all_rsw):
        for slot in all_rsw:
            if slot == 'pf1':
                assert all_rsw[slot].hands_dict['AA'].n_hand_combos == 6
            else:
                assert all_rsw[slot].hands_dict['AA'].n_hand_combos == 3

    def test_deselected_card_remove_removed_combos(self, all_csw, all_rsw):
        all_csw['hero'].cards_dict['Ad'].button.invoke()
        all_csw['hero'].cards_dict['Kc'].button.invoke()
        for slot in all_rsw:
            for hand in all_rsw[slot].hands_dict:
                assert all_rsw[slot].hands_dict[hand].removed_combos == []


# @pytest.mark.isolate
class TestFinalTest:
    def test_selected_hero_cards_pf1_total_combos_equal_1326(self, all_csw, all_rsw):
        all_csw['hero'].cards_dict['Ad'].button.invoke()    
        all_csw['hero'].cards_dict['Kh'].button.invoke()    
        all_rsw['pf1'].show()
        assert all_rsw['pf1'].total_combos == 1326

    def test_selected_hero_cards_pf2_total_combos_equal_1225(self, all_csw, all_rsw):
        all_rsw['pf2'].show()
        assert all_rsw['pf2'].total_combos == 1225

    def test_pf1_range_selected_combos_equal_400(self, all_rsw):
        pf1_range = ['JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22',
                    'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s', 
                    'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'QJs', 'QTs', 'Q9s', 'Q8s', 
                    'JTs', 'J9s', 'J8s', 'T9s', 'T8s', '98s', '97s', '87s', '76s',
                    'AJo', 'ATo', 'A9o', 'A8o', 'A7o', 'A6o', 'A5o', 'A4o', 'A3o', 'A2o',
                    'KQo', 'KJo', 'KTo', 'K9o', 'QJo', 'QTo', 'JTo', 'T9o', '98o']

        all_rsw['pf1'].color_buttons['1'].invoke()
        for hand in pf1_range:
            all_rsw['pf1'].hands_dict[hand].button.invoke()
        assert all_rsw['pf1'].selected_combos == 400
        all_rsw['pf1'].color_buttons['1'].invoke()

    def test_pf1_percent_hands_selected_equal_30(self, all_rsw):
        assert round(all_rsw['pf1'].percent_hands_selected, 0) == 30


if __name__ == '__main__':
    pytest.main()
