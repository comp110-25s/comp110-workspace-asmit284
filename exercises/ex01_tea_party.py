"""The purpose of this exercise is to create a program that calculates the information needed to host a tea party when given the number of guests who will attend."""

__author__: str = "730548173"


def main_planner(guests: int) -> None:
    """Call each function and produce printed output."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Compute the # of tea bags needed based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Compute the # of treats needed based on the number of guests."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of the tea bags and the treats combined."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
