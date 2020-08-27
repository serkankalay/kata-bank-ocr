from bank_ocr import Digit, split_digits

ONE_TO_NINE = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""


def test_split_digits():
    digits = split_digits(ONE_TO_NINE)
    print(digits)
    assert len(digits) == 9 and all(isinstance(d, Digit) for d in digits)
