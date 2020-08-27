import pytest

from bank_ocr import Digit, parse, split_digits

ONE_TO_NINE = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""


@pytest.fixture
def digit_0() -> Digit:
    return Digit(first_line=" _ ", second_line="| |", third_line="|_|",)


@pytest.fixture
def digit_1() -> Digit:
    return Digit(first_line="   ", second_line="  |", third_line="  |",)


@pytest.fixture
def digit_2() -> Digit:
    return Digit(first_line=" _ ", second_line=" _|", third_line="|_ ",)


@pytest.fixture
def digit_3() -> Digit:
    return Digit(first_line=" _ ", second_line=" _|", third_line=" _|",)


@pytest.fixture
def digit_4() -> Digit:
    return Digit(first_line="   ", second_line="|_|", third_line="  |",)


@pytest.fixture
def digit_5() -> Digit:
    return Digit(first_line=" _ ", second_line="|_ ", third_line=" _|",)


@pytest.fixture
def digit_6() -> Digit:
    return Digit(first_line=" _ ", second_line="|_ ", third_line="|_|",)


@pytest.fixture
def digit_7() -> Digit:
    return Digit(first_line=" _ ", second_line="  |", third_line="  |",)


@pytest.fixture
def digit_8() -> Digit:
    return Digit(first_line=" _ ", second_line="|_|", third_line="|_|",)


@pytest.fixture
def digit_9() -> Digit:
    return Digit(first_line=" _ ", second_line="|_|", third_line=" _|",)


def test_split_digits(
    digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9
):
    digits = split_digits(ONE_TO_NINE)
    print(digits)
    assert (
        len(digits) == 9
        and all(isinstance(d, Digit) for d in digits)
        and digits[0] == digit_1
        and digits[1] == digit_2
        and digits[2] == digit_3
        and digits[3] == digit_4
        and digits[4] == digit_5
        and digits[5] == digit_6
        and digits[6] == digit_7
        and digits[7] == digit_8
        and digits[8] == digit_9
    )


@pytest.mark.parametrize(
    "input_digit,parsed_number",
    [
        (pytest.lazy_fixture("digit_0"), 0),
        (pytest.lazy_fixture("digit_1"), 1),
        (pytest.lazy_fixture("digit_2"), 2),
        (pytest.lazy_fixture("digit_3"), 3),
        (pytest.lazy_fixture("digit_4"), 4),
        (pytest.lazy_fixture("digit_5"), 5),
        (pytest.lazy_fixture("digit_6"), 6),
        (pytest.lazy_fixture("digit_7"), 7),
        (pytest.lazy_fixture("digit_8"), 8),
        (pytest.lazy_fixture("digit_9"), 9),
    ],
)
def test_parse_digit(input_digit, parsed_number):
    assert parse(input_digit) == parsed_number
