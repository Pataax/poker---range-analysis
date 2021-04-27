import pytest
from app import app


def test_poker_range_analysis_layout():
    app.root.after(1, app.root.destroy())