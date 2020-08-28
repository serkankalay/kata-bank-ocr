from dataclasses import dataclass, replace
from enum import Enum, auto
from functools import reduce
from itertools import chain
from typing import Collection, List, Sequence

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


def _alter_digit(
    digit: Digit, row_index: int, char_index: int, char: str
) -> "Digit":
    if row_index == 0:
        return replace(
            digit, first_line=_replace_at(digit.first_line, char_index, char)
        )
    elif row_index == 1:
        return replace(
            digit,
            second_line=_replace_at(digit.second_line, char_index, char),
        )
    elif row_index == 2:
        return replace(
            digit, third_line=_replace_at(digit.third_line, char_index, char)
        )
    else:
        raise IndexError("Violated row number")


class Status(Enum):
    OK = auto()
    ILL = auto()
    ERR = auto()
    AMB = auto()


@dataclass(frozen=True)
class Account:
    numbers: Sequence[int]
    status: Status
    alternatives: List[Collection[int]] = None


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


def _is_valid_checksum(numbers: Sequence[int]) -> bool:
    return _checksum(numbers) == 0


def _variants_for_replacement(digit: Digit, char: str) -> Sequence[Digit]:
    return [
        _alter_digit(digit, row_index, index, char)
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
    return [number for number in variants if number >= 0]


def _replace_at_index(
    list_in: List[int], index: int, new_value: int
) -> Collection[int]:
    return list_in[0:index] + [new_value] + list_in[index + 1 :]


def parse(input_str: str) -> Account:
    # Calculate helpers
    digits = _split_digits(input_str)
    parsed = [_parse_digit(digit) for digit in digits]
    is_ill = any(number < 0 for number in parsed)
    is_valid_checksum = False if is_ill else _checksum(parsed) == 0

    if is_ill is False and is_valid_checksum is True:
        return Account(numbers=parsed, status=Status.OK,)
    elif is_ill is True:
        return Account(
            numbers=parsed,
            status=Status.ILL,
            alternatives=list(
                filter(
                    _is_valid_checksum,
                    [
                        _replace_at_index(parsed, index, variant)
                        for index, number in enumerate(parsed)
                        if number < 0
                        for variant in _variants(digits[index])
                    ],
                )
            ),
        )
    elif is_valid_checksum is False:
        return Account(
            numbers=parsed,
            status=Status.ERR,
            alternatives=list(
                filter(
                    _is_valid_checksum,
                    [
                        _replace_at_index(parsed, index, variant)
                        for index, number in enumerate(parsed)
                        for variant in _variants(digits[index])
                    ],
                )
            ),
        )
    else:
        raise NotImplementedError("Not a valid use case")
