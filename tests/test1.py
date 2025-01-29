import pytest

from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 2) == 4
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(-3, 3) == -9

    def test_add_calculate_correctly(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(5.5, 4.5) == 10.0

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(5, 3) == 2
        assert self.calc.subtraction(0, 5) == -5
        assert self.calc.subtraction(10, 10) == 0

    def test_division_calculate_correctly(self):
        assert self.calc.division(10, 2) == 5
        assert self.calc.division(-9, 3) == -3
        assert self.calc.division(7.5, 2.5) == 3.0

    def test_division_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.division(10, 0)