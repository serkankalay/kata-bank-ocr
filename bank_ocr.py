from dataclasses import dataclass

DIGIT_LENGTH = 3
NUMBER_OF_ROWS = 3


@dataclass(frozen=True)
class Digit:
    first_line: str
    second_line: str
    third_line: str


def split_digits(input_str: str):
    lines = input_str.splitlines()[1 : NUMBER_OF_ROWS + 1]
    return [
        Digit(
            first_line=lines[0][section_start : section_start + DIGIT_LENGTH],
            second_line=lines[1][section_start : section_start + DIGIT_LENGTH],
            third_line=lines[2][section_start : section_start + DIGIT_LENGTH],
        )
        for section_start in range(0, len(lines[0]), DIGIT_LENGTH)
    ]
