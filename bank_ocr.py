from dataclasses import dataclass

DIGIT_LENGTH = 3
NUMBER_OF_ROWS = 3

@dataclass(frozen=True)
class Digit:
    first_line: str
    second_line: str
    third_line: str


def split_digits(input_str: str):
    return [
        Digit(first_line=line[section_start:section_start+DIGIT_LENGTH], second_line="", third_line="")
        for line in input_str.splitlines()[0:NUMBER_OF_ROWS]
        for section_start in range(0, len(line), DIGIT_LENGTH)
    ]
