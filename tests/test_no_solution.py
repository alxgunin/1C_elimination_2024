import sys
sys.path.append('..')
from game import *

def test_no_solution():
    state = [CARD_VALUES[::-1]] * CARD_COUNTS
    print(state)
    assert Solitaire(state).process() == "No solution"
