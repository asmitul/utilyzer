from utilyzer.str_to_number import str_to_number


def test_str_to_number_integers():
    # Test positive integers
    assert str_to_number("123") == 123
    assert isinstance(str_to_number("123"), int)

    # Test zero
    assert str_to_number("0") == 0
    assert isinstance(str_to_number("0"), int)

    # Test negative integers
    assert str_to_number("-456") == -456
    assert isinstance(str_to_number("-456"), int)


def test_str_to_number_floats():
    # Test positive floats
    assert str_to_number("12.34") == 12.34
    assert isinstance(str_to_number("12.34"), float)

    # Test negative floats
    assert str_to_number("-12.34") == -12.34
    assert isinstance(str_to_number("-12.34"), float)

    # Test zero as float
    assert str_to_number("0.0") == 0.0
    assert isinstance(str_to_number("0.0"), float)

    # Test scientific notation
    assert str_to_number("1e-10") == 1e-10
    assert isinstance(str_to_number("1e-10"), float)


def test_str_to_number_invalid_inputs():
    # Test invalid string inputs
    assert str_to_number("abc") is None
    assert str_to_number("12.34.56") is None
    assert str_to_number("") is None
    assert str_to_number(" ") is None
    assert str_to_number("12abc") is None
    assert str_to_number("abc123") is None
    assert str_to_number("12.34.56") is None
    assert str_to_number("+-123") is None
    assert str_to_number("12..34") is None


def test_str_to_number_edge_cases():
    # Test whitespace handling
    assert str_to_number(" 123 ") == 123  # Should handle leading/trailing spaces
    assert str_to_number("\t456\n") == 456  # Should handle other whitespace

    # Test very large numbers
    assert str_to_number("999999999999999") == 999999999999999
    assert str_to_number("1e308") == 1e308


def test_str_to_number_non_string_inputs():
    # Test None
    assert str_to_number(None) is None

    # Test numeric inputs
    assert str_to_number(123) == 123
    assert str_to_number(12.34) == 12.34

    # Test other types
    assert str_to_number([1, 2, 3]) is None
    assert str_to_number({"key": "value"}) is None

    # Test boolean
    assert str_to_number(True) == 1
    assert str_to_number(False) == 0
