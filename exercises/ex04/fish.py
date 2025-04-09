"""File to define Fish class."""

__author__: str = "730548173"


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self) -> None:
        """Increases the age of the fish after one day."""
        self.age += 1
