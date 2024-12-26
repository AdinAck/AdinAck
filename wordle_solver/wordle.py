from abc import ABCMeta, abstractmethod

from ranked_letter import RankedLetter

class Wordle(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, WORD_LENGTH: int, GUESS_COUNT: int):
        ...
        
    @abstractmethod
    def guess(self, word: str) -> bool:
        ...
    
    @abstractmethod
    def get_state(self) -> tuple[list[list[RankedLetter]], bool]:
        ...