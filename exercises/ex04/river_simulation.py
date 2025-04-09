"""File to run R class."""

__author__: str = "730548173"


from exercises.ex04.river import River
from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


my_river = River(10, 2)


my_river.view_river()

my_river.one_river_week()
