"""The purpose of this exercise is to practice dictionary functions."""

__author__: str = "730548173"


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


import pytest

"""invert function unit tests"""


def test_invert1() -> None:
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert2() -> None:
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert3() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


"""count function unit tests"""


def test_count1() -> None:
    assert count([]) == {}


def test_count2() -> None:
    assert count(["pink", "purple", "blue"]) == {"blue": 1, "purple": 1, "pink": 1}


def test_count3() -> None:
    assert count(["pear", "banana", "pear", "kiwi", "banana", "pear"]) == {
        "pear": 3, "banana": 2, "kiwi": 1}


"""favorite_color function unit tests"""


def test_favorite_color1() -> None:
    assert favorite_color({}) == ""


def test_favorite_color2() -> None:
    assert favorite_color({"Adam": "blue", "Bob": "red", "Ashley": "blue", 
    "Sarah": "green"}) == "blue"


def test_favorite_color3() -> None:
    assert favorite_color({"Adam": "red", "Bob": "red", "Ashley": "blue", 
    "John": "blue"}) == "red"


"""bin_len function unit tests"""


def test_bin_len1() -> None:
    assert bin_len([]) == {}


def test_bin_len2() -> None:
    assert bin_len(["koala", "lizard", "koala", "rabbit", "lizard", "emu"]) == {5: 
    {"koala"}, 6: {"lizard", "rabbit"}, 3: {"emu"}}


def test_bin_len3() -> None:
    assert bin_len(["tree", "mountain", "river", "cloud", "sky"]) == {4: 
    {"tree"}, 8: {"mountain"}, 5: {"river", "cloud"}, 3: {"sky"}}

