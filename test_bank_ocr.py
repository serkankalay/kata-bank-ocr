from bank_ocr import Digit, split_digits

ONE_TO_NINE_LINE_1 = "    _  _     _  _  _  _  _ "


def test_split_digits():
    digits = split_digits(ONE_TO_NINE_LINE_1)
    assert len(digits) == 9 and all(isinstance(d, Digit) for d in digits)
