import pytest

from bank_ocr import (Digit, Status, _alter_digit, _checksum, _parse_digit,
                      _split_digits, _variants, parse)

ZERO_TO_NINE = """
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|

"""


def _get_from_order(input_str: str, order: int) -> str:
    return "".join(
        line if index == 3 else line[order * 3 : (order * 3) + 3] + "\n"
        for index, line in enumerate(input_str[1:].splitlines())
    )


@pytest.fixture
def zero() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 0))[0]


@pytest.fixture
def one() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 1))[0]


@pytest.fixture
def two() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 2))[0]


@pytest.fixture
def three() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 3))[0]


@pytest.fixture
def four() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 4))[0]


@pytest.fixture
def five() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 5))[0]


@pytest.fixture
def six() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 6))[0]


@pytest.fixture
def seven() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 7))[0]


@pytest.fixture
def eight() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 8))[0]


@pytest.fixture
def nine() -> Digit:
    return _split_digits(_get_from_order(ZERO_TO_NINE, 9))[0]


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
    digits = _split_digits(one_to_nine)
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
    assert _parse_digit(input_digit) == parsed_number


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
    assert parse(input_str).numbers == parsed_numbers


def test_checksum():
    assert _checksum([3, 4, 5, 8, 8, 2, 8, 6, 5]) == 0


FIFTY_ONE = """
 _  _  _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
                           
"""


@pytest.fixture
def fifty_one() -> str:
    return FIFTY_ONE[1:]


ILL_1 = """
    _  _  _  _  _  _     _ 
|_||_|| || ||_   |  |  | _ 
  | _||_||_||_|  |  |  | _|
                           
"""


@pytest.fixture
def ill_1() -> str:
    return ILL_1[1:]


ILL_2 = """
    _  _     _  _  _  _  _ 
  | _| _||_| _ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _ 
                           
"""


@pytest.fixture
def ill_2() -> str:
    return ILL_2[1:]


ERR = """
 _  _     _  _        _  _ 
|_ |_ |_| _|  |  ||_||_||_ 
|_||_|  | _|  |  |  | _| _|

"""


@pytest.fixture
def err() -> str:
    return ERR[1:]


def test_parse_check(fifty_one):
    account = parse(fifty_one)
    assert account.status is Status.OK


def test_parse_ill_1(ill_1):
    account = parse(ill_1)
    assert account.status is Status.ILL and account.numbers == [
        4,
        9,
        0,
        0,
        6,
        7,
        7,
        1,
        -1,
    ]


def test_parse_ill_2(ill_2):
    account = parse(ill_2)
    assert account.status is Status.ILL and account.numbers == [
        1,
        2,
        3,
        4,
        -1,
        6,
        7,
        8,
        -1,
    ]


def test_parse_err(err):
    account = parse(err)
    assert account.status is Status.ERR


@pytest.mark.parametrize(
    "input_digit,expected_variants",
    [
        (pytest.lazy_fixture("zero"), [8]),
        (pytest.lazy_fixture("one"), [7]),
        (pytest.lazy_fixture("two"), []),
        (pytest.lazy_fixture("three"), [9]),
        (pytest.lazy_fixture("four"), []),
        (pytest.lazy_fixture("five"), [6, 9]),
        (pytest.lazy_fixture("six"), [5, 8]),
        (pytest.lazy_fixture("seven"), [1]),
        (pytest.lazy_fixture("eight"), [0, 6, 9]),
        (pytest.lazy_fixture("nine"), [3, 5, 8]),
    ],
)
def test_variants(input_digit, expected_variants):
    assert sorted(_variants(input_digit)) == expected_variants


def test_alter_digit_eight(eight):
    assert _alter_digit(eight, 1, 1, " ") == Digit(
        first_line=" _ ", second_line="| |", third_line="|_|"
    )
