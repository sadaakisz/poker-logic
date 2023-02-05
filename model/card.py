import functools
from enum import Enum
class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Symbol(Enum):
    DIAMONDS = 'D'
    CLUBS = 'C'
    HEARTS = 'H'
    SPADES = 'S'

# https://docs.python.org/3/library/functools.html#functools.total_ordering
@functools.total_ordering
class Card:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
    
    def _is_valid_operand(self, other):
        return (hasattr(other, 'value') and
                hasattr(other, 'symbol'))
    
    def __eq__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.value == other.value)
    def __lt__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.value < other.value)
    
    def __repr__(self) -> str:
        return str(self.value)+self.symbol