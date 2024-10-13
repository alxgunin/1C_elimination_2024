import pytest
import sys
sys.path.append('..')
from game import *

def test_bad_initial_state():
    state = [[10] * 9] * 8
    with pytest.raises(AssertionError):
        assert Solitaire(state)

def test_initial_state_is_final():
    state = [CARD_VALUES] * CARD_COUNTS
    assert Solitaire(state).process() == "Found solution in 0 iterations"
