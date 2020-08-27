from dataclasses import dataclass
from functools import reduce
from typing import Sequence

DIGIT_LENGTH = 3
NUMBER_OF_ROWS = 3


FIRST_LINE_MAPPING = {
    "   ": {1, 4},
    " _ ": {0, 2, 3, 5, 6, 7, 8, 9},
}

SECOND_LINE_MAPPING = {
    "| |": {0},
    "  |": {1, 7},
    " _|": {2, 3},
    "|_|": {4, 8, 9},
    "|_ ": {5, 6},
}

THIRD_LINE_MAPPING = {
    "|_|": {0, 6, 8},
    "  |": {1, 4, 7},
    "|_ ": {2},
    " _|": {3, 5, 9},
}


LINE_MAPPINGS = {
    0: FIRST_LINE_MAPPING,
    1: SECOND_LINE_MAPPING,
    2: THIRD_LINE_MAPPING,
}


@dataclass(frozen=True)
class Digit:
    first_line: str
    second_line: str
    third_line: str


def split_digits(input_str: str) -> Sequence[Digit]:
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


def parse_digit(digit: Digit) -> int:
    return reduce(
        set.intersection,
        (
            LINE_MAPPINGS[i][line]
            for i, line in enumerate(
                [digit.first_line, digit.second_line, digit.third_line]
            )
        ),
    ).pop()


def parse(input_str: str) -> Sequence[int]:
    return [parse_digit(digit) for digit in split_digits(input_str)]
