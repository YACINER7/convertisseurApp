from app_functions import convert

RATES = {"EUR": 1.0, "USD": 1.1, "JPY": 130.0, "GBP": 0.85, "CAD": 1.5}


def test_convert_eur_to_usd():
    assert round(convert(10, "EUR", "USD", RATES), 2) == 11.0


def test_convert_usd_to_eur():
    assert round(convert(11, "USD", "EUR", RATES), 2) == 10.0


def test_convert_same_currency():
    assert convert(10, "EUR", "EUR", RATES) == 10


def test_convert_zero_amount():
    assert convert(0, "EUR", "USD", RATES) is None


def test_convert_negative_amount():
    assert convert(-5, "EUR", "USD", RATES) is None
