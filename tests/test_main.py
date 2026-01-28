from src.main import add_function, subtract_function


def test_add_function():
    assert add_function(10, 20) == 30
    assert add_function(0, 0) == 0
    assert add_function(0, 1) == 1


def test_subtract_function():
    assert subtract_function(10, 20) == -10
    assert subtract_function(0, 0) == 0
    assert subtract_function(0, 1) == -1
