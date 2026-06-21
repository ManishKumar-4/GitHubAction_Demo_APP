# Import the functions to be tested from the math_operations module
from src.math_operations import add, sub


def test_add():
    """
    Test cases for the add() function.
    Verifies that addition works correctly for both
    positive and negative numbers.
    """

    # Test addition of two positive integers
    assert add(2, 3) == 5

    # Test addition resulting in zero
    assert add(-1, 1) == 0


def test_sub():
    """
    Test cases for the sub() function.
    Verifies correct subtraction results for various scenarios.
    """

    # Test subtraction where the result is positive
    assert sub(5, 3) == 2

    # Test another positive subtraction result
    assert sub(4, 3) == 1

    # Test subtraction resulting in zero
    assert sub(3, 3) == 0

    # Test subtraction resulting in a negative number
    assert sub(2, 3) == -1