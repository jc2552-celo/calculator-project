import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_multiply():
    assert calculator.multiply(2, 4) == 8

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        calculator.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
