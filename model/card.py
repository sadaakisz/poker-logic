import functools
from enum import Enum
class Value(Enum):
    """
    Enum with card name and value.

    List(Value) returns a list containing the <Name:Value> pairs.

    List(Value)[x].name returns the card name in string

    and List(Value)[x].value returns integer value.
    """

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
    """
    Enum with card symbol name and single letter string.

    List(Symbol) returns a list containing the <SymbolName:Symbol> pairs.

    List(Symbol)[x].name returns the symbol name in string

    and List(Symbol)[x].value returns integer value.
    """

    DIAMONDS = 'D'
    CLUBS = 'C'
    HEARTS = 'H'
    SPADES = 'S'

# https://docs.python.org/3/library/functools.html#functools.total_ordering
@functools.total_ordering
class Card:
    """
    Class representing a playing card.

    Can be initialized by passing a single string: eg. '13C' for King of Clubs.

    OR

    Can be initialized by passing a Value.value and Symbol.value.

    The initializer does NOT check if the card is a valid playing card yet.
    """
    def __init__(self, *args) -> None:
        if len(args)==2:
            self.value = args[0]
            self.symbol = args[1]
        if len(args)==1 and isinstance(args[0], str):
            str_card = args[0]
            if len(str_card)==3:
                self.value = int(str_card[:2])
                self.symbol = str_card[-1:]
            if len(str_card)==2:
                self.value = int(str_card[:1])
                self.symbol = str_card[-1:]
        else:
            self.value = 0
            self.symbol = 'NA'

    def _is_valid_operand(self, other) -> None:
        return (hasattr(other, 'value') and
                hasattr(other, 'symbol'))

    def __eq__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.value == other.value
    def __lt__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.value < other.value

    def __repr__(self) -> str:
        return str(self.value)+self.symbol

    def as_str(self) -> str:
        """
        Returns card as a string.

        eg. Queen of Hearts returns '12H'.
        """
        return str(self.value)+self.symbol

    def as_tuple(self) -> tuple:
        """Returns tuple: (value, symbol)"""
        return (self.value, self.symbol)
