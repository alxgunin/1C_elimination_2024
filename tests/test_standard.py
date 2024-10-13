import sys
sys.path.append('..')
from game import *

def test_correct_value1():
    state = [
    REMOVABLE_STATE,
    REMOVABLE_STATE,
    REMOVABLE_STATE,
    REMOVABLE_STATE,
    REMOVABLE_STATE,
    REMOVABLE_STATE,
    [7, 7, 8, 9, 10, 11, 12, 13, 14],
    [6, 6, 8, 9, 10, 11, 12, 13, 14],
    ]
    assert Solitaire(state).process() == "Found solution in 5 iterations"
