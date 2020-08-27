import pytest

from bank_ocr import Digit, parse, parse_digit, split_digits

ONE_TO_NINE = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

"""


@pytest.fixture
def one_to_nine() -> str:
    return ONE_TO_NINE[1:]


ZEROS = """
 _  _  _  _  _  _  _  _  _ 
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
                           
"""


@pytest.fixture
def zeros() -> str:
    return ZEROS[1:]


ONES = """
                           
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                           
"""


@pytest.fixture
def ones() -> str:
    return ONES[1:]


TWOS = """
 _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
                           
"""


@pytest.fixture
def twos() -> str:
    return TWOS[1:]


THREES = """
 _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|
                           
"""


@pytest.fixture
def threes() -> str:
    return THREES[1:]


FOURS = """
                           
|_||_||_||_||_||_||_||_||_|
  |  |  |  |  |  |  |  |  |
                           
"""


@pytest.fixture
def fours() -> str:
    return FOURS[1:]


FIVES = """
 _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
 _| _| _| _| _| _| _| _| _|
                           
"""


@pytest.fixture
def fives() -> str:
    return FIVES[1:]


SIXES = """
 _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
|_||_||_||_||_||_||_||_||_|
                           
"""


@pytest.fixture
def sixes() -> str:
    return SIXES[1:]


SEVENS = """
 _  _  _  _  _  _  _  _  _ 
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                           
"""


@pytest.fixture
def sevens() -> str:
    return SEVENS[1:]


EIGHTS = """
 _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|
                           
"""


@pytest.fixture
def eights() -> str:
    return EIGHTS[1:]


NINES = """
 _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|
                           
"""


@pytest.fixture
def nines() -> str:
    return NINES[1:]


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
    one_to_nine,
    digit_1,
    digit_2,
    digit_3,
    digit_4,
    digit_5,
    digit_6,
    digit_7,
    digit_8,
    digit_9,
):
    digits = split_digits(one_to_nine)
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
    assert parse_digit(input_digit) == parsed_number


@pytest.mark.parametrize(
    "input_str,parsed_numbers",
    [
        (pytest.lazy_fixture("one_to_nine"), [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (pytest.lazy_fixture("zeros"), [0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (pytest.lazy_fixture("ones"), [1, 1, 1, 1, 1, 1, 1, 1, 1]),
        (pytest.lazy_fixture("twos"), [2, 2, 2, 2, 2, 2, 2, 2, 2]),
        (pytest.lazy_fixture("threes"), [3, 3, 3, 3, 3, 3, 3, 3, 3]),
        (pytest.lazy_fixture("fours"), [4, 4, 4, 4, 4, 4, 4, 4, 4]),
        (pytest.lazy_fixture("fives"), [5, 5, 5, 5, 5, 5, 5, 5, 5]),
        (pytest.lazy_fixture("sixes"), [6, 6, 6, 6, 6, 6, 6, 6, 6]),
        (pytest.lazy_fixture("sevens"), [7, 7, 7, 7, 7, 7, 7, 7, 7]),
        (pytest.lazy_fixture("eights"), [8, 8, 8, 8, 8, 8, 8, 8, 8]),
        (pytest.lazy_fixture("nines"), [9, 9, 9, 9, 9, 9, 9, 9, 9]),
    ],
)
def test_parse_use_cases_1(input_str, parsed_numbers):
    assert parse(input_str) == parsed_numbers
