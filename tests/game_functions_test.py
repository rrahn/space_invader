import pytest

from dataclasses import dataclass
from src.game_functions import get_number_rows

@dataclass
class TestSettings():
    __test__ = False
    screen_height = 600

def test_get_number_rows():
    assert get_number_rows(TestSettings(), 80, 50) == 3
    assert get_number_rows(TestSettings(), 20, 20) == 4
