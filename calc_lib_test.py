import calc_lib

def test_calc_handles_addition():
    expression = "1 + 3"
    assert calc_lib.calc(expression) == 4

def test_calc_handles_subtraction():
    expression = "3 - 1"
    assert calc_lib.calc(expression) == 2

def test_calc_handles_multiplication():
    expression = "2 * 3"
    assert calc_lib.calc(expression) == 6

def test_calc_handles_division():
    expression = "6 / 3"
    assert calc_lib.calc(expression) == 2

def test_calc_handles_large_numbers():
    expression = "1000000000 + 1000000000"
    assert calc_lib.calc(expression) == 2000000000

def test_calc_handles_negative_numbers():
    expression = "-1 + 3"
    assert calc_lib.calc(expression) == 2

def test_calc_handles_decimal_numbers():
    expression = "1.5 + 3.5"
    assert calc_lib.calc(expression) == 5.0

def test_calc_handles_parentheses():
    expression = "(1 + 3) * 2"
    assert calc_lib.calc(expression) == 8


