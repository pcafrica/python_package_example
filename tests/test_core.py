import pytest
import my_package as my_pkg

def test_mean():
    numbers = [10, 20, 30]
    expected = 20
    assert my_pkg.mean(numbers) == expected
