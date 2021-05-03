import pytest, tkinter
from app import PokerRangeAnalysis, CardSelectionWindow, Cards


@pytest.fixture
def app():
    return PokerRangeAnalysis()

@pytest.fixture
def hero_csw():
    return CardSelectionWindow('hero')


class TestGeneralParametersCardSelectionWindow:
    def test_inicial_value_list_select_cards(self, hero_csw):
        assert hero_csw.selected_cards == []
    
    def test_card_dict_len(self, hero_csw):
        assert len(hero_csw.card_dict) == 52

    def test_type_stored_dict_instance(self, hero_csw):
        any_frame = tkinter.Frame()
        foo = Cards('bruno', 'Ax', 'green', any_frame, 0, 0)
        assert type(hero_csw.card_dict['Ad']) == type(foo)

    def test_card_selection_window_show_by_invoke(self, app, hero_csw):
        assert app.widgets['hero']['card_selection'].invoke() == \
            'the card selection window was displayed'

    def test_click_select_any_card_by_invoke(self, hero_csw):
        assert hero_csw.card_dict['Ad'].button.invoke() == 'the card button was clicked'

    def test_color_change_selected_card(self, hero_csw):
        assert hero_csw.card_dict['Ad'].button['bg'] == 'gray'
