import typing as tp
from copy import deepcopy
from queue import Queue
from collections import defaultdict

CARD_VALUES = list(range(6, 15))
CARD_COUNTS = 8
REMOVABLE_STATE = sorted(CARD_VALUES)
FINAL_STATE = [[]] * CARD_COUNTS
VALID_STATE_CNT = {x: CARD_COUNTS for x in CARD_VALUES}


class Solitaire():
    def __state_hash__(self, state: tp.Sequence[int]) -> int:
        """
        Calculate state hash
        :param state: sequence of cards in heaps
        :param result: state hash
        :return: hash
        """
        return hash(tuple(tuple(heap) for heap in state))

    def __clear__(self, state: tp.Sequence[int]) -> tp.Sequence[int]:
        """
        Removes full heaps from state
        :param state: sequence of cards in heaps
        :return: clered state
        """
        copied = deepcopy(state)
        for index, heap in enumerate(copied):
            if heap == REMOVABLE_STATE:
                copied[index] = []

        return copied
    
    def __is_valid__(self, state: tp.Sequence[int]) -> bool:
        """"
        Checks that given sequence is valid
        :param state: sequence of cards in heaps
        :result: True if valid, false otherwise
        """
        if len(state) != 8:
            return False

        cnt = defaultdict(int)

        for heap in state:
            if len(heap) != len(CARD_VALUES):
                return False

            for elem in heap:
                cnt[elem] += 1

        return dict(cnt) == VALID_STATE_CNT

    def __init__(self, state: tp.Sequence[int]) -> None:
        """"
        Constructor of class Game
        :param state: sequence of cards in heaps
        """
        assert self.__is_valid__(state)

        self.start_state = self.__clear__(state)
        self.start_hash = self.__state_hash__(self.start_state)
        self.dist = {self.start_hash: 0}

    def process(self) -> str:
        """
        Implementation of playing
        :return: result of processing game
        """
        queue = Queue()
        queue.put((self.start_state, self.start_hash))
        while not queue.empty():
            cur_state, cur_hash = queue.get()
            if cur_state == FINAL_STATE:
                return f"Found solution in {self.dist[cur_hash]} iterations"

            for i, frm in enumerate(cur_state):
                if len(frm) == 0:
                    continue

                for j, to in enumerate(cur_state):
                    if i == j:
                        continue

                    if len(to) == 0 or frm[0] < to[0]:
                        new_state = deepcopy(cur_state)
                        new_state[j].insert(0, frm[0])

                        del new_state[i][0]
                        new_state = self.__clear__(new_state)

                        new_hash = self.__state_hash__(new_state)
                        if new_hash not in self.dist or self.dist[new_hash] > self.dist[cur_hash] + 1:
                            self.dist[new_hash] = self.dist[cur_hash] + 1
                            queue.put((new_state, new_hash))

        return "No solution"
