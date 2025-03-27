"""The purpose of this exercise is to practice dictionary functions."""

__author__: str = "730548173"


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


import pytest

"""invert function unit tests"""


def test_invert1() -> None:
    """Tests if invert correctly swaps keys and values in a dictionary."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert2() -> None:
    """Tests if invert correctly handles a single key-value pair."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert3() -> None:
    """Tests if invert raises a KeyError when duplicate values exist in 
    the input dictionary."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)  


"""count function unit tests"""


def test_count1() -> None:
    """Tests if count raises a KeyError when given an empty list."""
    with pytest.raises(KeyError):
        count([])


def test_count2() -> None:
    """Tests if count correctly counts unique items in a list with no duplicates."""
    assert count(["pink", "purple", "blue"]) == {"blue": 1, "purple": 1, "pink": 1}


def test_count3() -> None:
    """Tests if count correctly counts occurrences of duplicate items in a list."""
    assert count(["pear", "banana", "pear", "kiwi", "banana", "pear"]) == {
        "pear": 3, "banana": 2, "kiwi": 1}


"""favorite_color function unit tests"""


def test_favorite_color1() -> None:
    """Test if favorite_color raises a KeyError for an empty dictionary."""
    with pytest.raises(KeyError):
        favorite_color({})


def test_favorite_color2() -> None:
    """Test if favorite_color returns the most frequent color."""
    assert favorite_color({"Adam": "blue", "Bob": "red", "Ashley": "blue", 
    "Sarah": "green"}) == "blue"


def test_favorite_color3() -> None:
    """Test if favorite_color returns the most frequent color when there's a tie."""
    assert favorite_color({"Adam": "red", "Bob": "red", "Ashley": "blue", 
    "John": "blue"}) == "red"


"""bin_len function unit tests"""


def test_bin_len1() -> None:
    """Test if bin_len raises a KeyError for an empty list."""
    with pytest.raises(KeyError):
        bin_len([])


def test_bin_len2() -> None:
    """Test if bin_len groups words by their length with duplicate words."""
    assert bin_len(["koala", "lizard", "koala", "rabbit", "lizard", "emu"]) == {5: 
    {"koala"}, 6: {"lizard", "rabbit"}, 3: {"emu"}}


def test_bin_len3() -> None:
    """Test that `bin_len` correctly groups words by their length."""
    assert bin_len(["tree", "mountain", "river", "cloud", "sky"]) == {4: 
    {"tree"}, 8: {"mountain"}, 5: {"river", "cloud"}, 3: {"sky"}}

