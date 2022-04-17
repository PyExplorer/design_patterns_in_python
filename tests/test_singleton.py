"""Tests for classes with singleton pattern."""
from copy import deepcopy

from src.design_patterns_in_python.singleton import Database
from src.design_patterns_in_python.singleton import SingletonAccounting


class TestSingleton:
    """Test case for singleton."""

    test_db = {"store_1": 10, "store_2": 30, "store_3": 100}
    test_file = "tests/test_revenues.txt"

    def test_is_singleton(self) -> None:
        """Check if this is the same object."""
        db_1 = Database(dict_db=self.test_db)
        db_2 = Database(dict_db=self.test_db)
        assert db_1 is db_2
        Database.drop_instances()

    def test_is_not_singleton(self) -> None:
        """Check if this is not the same object."""
        db_1 = Database(dict_db=self.test_db)
        db_2 = deepcopy(db_1)
        assert db_1 is not db_2
        Database.drop_instances()

    def test_singleton_total_revenue(self) -> None:
        """Check if calculating total revenue from dict db works well."""
        dummy_db = Database(dict_db=self.test_db)
        sa = SingletonAccounting(dummy_db)
        assert sa.total_revenue(["store_1", "store_3"]) == 110
        Database.drop_instances()

    def test_singleton_total_revenue_file(self) -> None:
        """Check if calculating total revenue from local file db works well."""
        dummy_db = Database(path=self.test_file)
        sa = SingletonAccounting(dummy_db)
        assert sa.total_revenue(["store_1", "store_2"]) == 15000
        Database.drop_instances()

    def test_drop_instances(self) -> None:
        """Check if all instances are removed."""
        _ = Database(dict_db=self.test_db)
        Database.drop_instances()
        assert Database.is_clean() is True

    def test_drop_instances_failed(self) -> None:
        """Check if all instances are removed."""
        _ = Database(dict_db=self.test_db)
        Database.drop_instances()
        Database.drop_instances()
        assert Database.is_clean() is True
