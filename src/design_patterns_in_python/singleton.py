"""Singleton - a component which is instantiated only once."""
from __future__ import annotations  # pragma: no cover

from copy import deepcopy

FILE_PATH = "revenues.txt"


class MetaClassSingleton(type):
    """Meta class for singleton pattern."""

    _instances: dict[MetaClassSingleton, MetaClassSingleton] = {}

    def __call__(cls, *args, **kwargs) -> MetaClassSingleton:
        """Called before the actual instance is created."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print(f"Instantiated first time, class {cls.__name__}")
        else:
            print(f"Using existing class: {cls.__name__}")
        return cls._instances[cls]

    def drop_instances(cls) -> None:
        """Remove all instances to be able creating a new one."""
        try:
            del cls._instances[cls]
        except KeyError:
            pass

    def is_clean(cls):
        """Check if all instances are removed."""
        return not cls._instances


class Database(metaclass=MetaClassSingleton):
    """Database class."""

    def __init__(self, path: str = FILE_PATH, dict_db: dict = None) -> None:
        """DB initialization.

        :param path: path to local file with data
        :param dict_db: dict with data - used as optional when no local file needed.
        """
        self.revenue = {}

        if dict_db:
            self.revenue = deepcopy(dict_db)
            return

        f = open(path)
        lines = f.readlines()
        for i in range(0, len(lines)):
            name, revenue = lines[i].split(",")
            self.revenue[name.strip()] = float(revenue.strip())
        f.close()


class SingletonAccounting:
    """Class for calculations."""

    def __init__(self, db: Database) -> None:
        """Initialization."""
        self.db = db

    def total_revenue(self, stores: list) -> float:
        """Total revenue calculation."""
        revenue = 0
        for store in stores:
            revenue += self.db.revenue[store]
        return revenue


def main(path: str) -> None:  # pragma: no cover
    """Main."""
    db = Database(path)

    stores_1 = ["store_1", "store_2"]
    stores_2 = ["store_3", "store_4"]

    sa = SingletonAccounting(db)
    print(f"revenue for {stores_1}: {sa.total_revenue(stores_1)}")
    print(f"revenue for {stores_2}: {sa.total_revenue(stores_2)}")


if __name__ == "__main__":  # pragma: no cover
    file_path = "./data/revenues.txt"
    main(file_path)
