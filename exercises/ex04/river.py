"""File to define River class."""

__author__: str = "730548173"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove fish older than 3 and bears older than 5 from the river."""
        remaining_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                remaining_fish.append(fish)
        self.fish = remaining_fish

        remaining_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                remaining_bears.append(bear)
        self.bears = remaining_bears

    def remove_fish(self, amount: int) -> None:
        """Remove a certain amount of fish from the front of the list."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self) -> None:
        """The bear will eat 3 fish if there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove bears with a hunger_score lower than 0 from the river."""
        remaining_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                remaining_bears.append(bear)
        self.bears = remaining_bears

    def repopulate_fish(self) -> None:
        """Each pair of bears will produce 1 offspring."""
        num_of_offspring = len(self.bears) // 2
        for _ in range(num_of_offspring):
            self.bears.append(Bear())

    def repopulate_bears(self) -> None:
        """Each pair of fish will produce 4 offspring."""
        num_of_offspring = (len(self.fish) // 2) * 4
        for _ in range(num_of_offspring):
            self.fish.append(Fish())

    def view_river(self) -> None:
        """Print the status of the bear and fish populations in a given River object."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates 7 days of life in the river."""
        for _ in range(7):
            self.one_river_day()
