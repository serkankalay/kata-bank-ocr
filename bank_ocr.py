from dataclasses import dataclass, replace
from functools import reduce
from itertools import chain
from typing import Sequence

DIGIT_LENGTH = 3
NUMBER_OF_ROWS = 3

CHECKSUM_DIVISOR = 11


FIRST_LINE_MAPPING = {
    "   ": {1, 4},
    " _ ": {0, 2, 3, 5, 6, 7, 8, 9},
}

FIRST_LINE_KEYS = set(FIRST_LINE_MAPPING.keys())

SECOND_LINE_MAPPING = {
    "| |": {0},
    "  |": {1, 7},
    " _|": {2, 3},
    "|_|": {4, 8, 9},
    "|_ ": {5, 6},
}

SECONDS_LINE_KEYS = set(SECOND_LINE_MAPPING.keys())

THIRD_LINE_MAPPING = {
    "|_|": {0, 6, 8},
    "  |": {1, 4, 7},
    "|_ ": {2},
    " _|": {3, 5, 9},
}

THIRD_LINE_KEYS = set(THIRD_LINE_MAPPING.keys())


LINE_MAPPINGS = {
    0: FIRST_LINE_MAPPING,
    1: SECOND_LINE_MAPPING,
    2: THIRD_LINE_MAPPING,
}


def _replace_at(input_str: str, char_index: int, char: str) -> str:
    temp = list(input_str)
    temp[char_index] = char
    return "".join(temp)


@dataclass(frozen=True)
class Digit:
    first_line: str
    second_line: str
    third_line: str

    def line(self, index: int) -> str:
        if index == 0:
            return self.first_line
        elif index == 1:
            return self.second_line
        elif index == 2:
            return self.third_line
        else:
            raise IndexError("Violated row number")

    def alter(self, row_index: int, char_index: int, char: str) -> "Digit":
        if row_index == 0:
            return replace(
                self, first_line=_replace_at(self.first_line, char_index, char)
            )
        elif row_index == 1:
            return replace(
                self,
                second_line=_replace_at(self.second_line, char_index, char),
            )
        elif row_index == 2:
            return replace(
                self, third_line=_replace_at(self.third_line, char_index, char)
            )
        else:
            raise IndexError("Violated row number")


@dataclass(frozen=True)
class Account:
    numbers: Sequence[int]
    is_valid_checksum: bool
    is_ill: bool


def _split_digits(input_str: str) -> Sequence[Digit]:
    lines = input_str.splitlines()[0:NUMBER_OF_ROWS]
    print(lines)
    return [
        Digit(
            first_line=lines[0][section_start : section_start + DIGIT_LENGTH],
            second_line=lines[1][section_start : section_start + DIGIT_LENGTH],
            third_line=lines[2][section_start : section_start + DIGIT_LENGTH],
        )
        for section_start in range(0, len(lines[0]), DIGIT_LENGTH)
    ]


def _parse_digit(digit: Digit) -> int:
    try:
        return reduce(
            set.intersection,
            (
                LINE_MAPPINGS[i][line]
                for i, line in enumerate(
                    [digit.first_line, digit.second_line, digit.third_line]
                )
            ),
        ).pop()
    except KeyError:
        return -1


def _checksum(numbers: Sequence[int]) -> int:
    calculated_sum = 0
    for index, member in enumerate(reversed(numbers)):
        calculated_sum += (index + 1) * member

    return calculated_sum % CHECKSUM_DIVISOR


def parse(input_str: str) -> Account:
    parsed = [_parse_digit(digit) for digit in _split_digits(input_str)]
    is_ill = any(number < 0 for number in parsed)
    return Account(
        numbers=parsed,
        is_ill=is_ill,
        is_valid_checksum=False if is_ill else _checksum(parsed) == 0,
    )


def _variants_for_replacement(digit: Digit, char: str) -> Sequence[Digit]:
    return [
        digit.alter(row_index, index, char)
        for row_index in range(NUMBER_OF_ROWS)
        for index in range(DIGIT_LENGTH)
        if digit.line(row_index)[index] != char
    ]


def _variants(digit: Digit) -> Sequence[int]:
    variants = [
        _parse_digit(digit)
        for digit in chain(
            _variants_for_replacement(digit, "_"),
            _variants_for_replacement(digit, "|"),
            _variants_for_replacement(digit, " "),
        )
    ]
    return sorted([number for number in variants if number >= 0])
