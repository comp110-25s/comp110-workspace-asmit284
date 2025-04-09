"""File to define Bear class."""

__author__: str = "730548173"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Increases the age of the bear after one day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger_score based on number of fish eaten."""
        self.hunger_score += num_fish
