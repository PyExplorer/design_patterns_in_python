"""Tests for classes with composite pattern."""
from src.design_patterns_in_python.composite import BaseValue
from src.design_patterns_in_python.composite import ManyValues
from src.design_patterns_in_python.composite import SingleValue


class TestSingleValues:
    def test_sum_single_value(self) -> None:  # noqa: D105
        single_value = SingleValue(11)
        assert single_value.sum == 11

    def test_name_single_value(self) -> None:  # noqa: D105
        single_value = SingleValue(11)
        assert single_value.name == "Single value"

    def test_str_single_value(self) -> None:  # noqa: D105
        single_value = SingleValue(11)
        assert str(single_value) == "Single value: 11"


class TestManyValues:
    def test_sum_many_values(self) -> None:  # noqa: D105
        many_values = ManyValues()
        many_values.append(22)
        many_values.append(33)
        assert many_values.sum == 55

    def test_sum_composite_values(self) -> None:  # noqa: D105
        single_value = SingleValue(11)
        many_values = ManyValues()
        many_values.append(22)
        many_values.append(33)
        composite_values = ManyValues()
        composite_values.append(single_value)
        composite_values.append(many_values)

        assert composite_values.sum == 66

    def test_name_many_value(self) -> None:  # noqa: D105
        many_values = ManyValues()
        assert many_values.name == "Many values"


    def test_str_many_values(self):
        composite_values = ManyValues()
        composite_values.append(SingleValue(11))
        many_values = ManyValues()
        many_values.append(22)
        many_values.append(33)
        composite_values.append(many_values)
        assert str(composite_values) == "Many values: Single value: 11, Many values: 22, 33"
