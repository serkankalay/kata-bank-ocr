import pytest

from bank_ocr import Digit, split_digits

ONE_TO_NINE = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""


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


@pytest.fixture
def digit_0() -> Digit:
    return Digit(first_line=" _ ", second_line="| |", third_line="|_|",)


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
