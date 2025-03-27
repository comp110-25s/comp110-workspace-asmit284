"""The purpose of this exercise is to practice defining unit test functions."""

__author__: str = "730548173"


def invert(a: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and values in my dictionary."""
    invert_dict = {}
    for key in a:
        if key in a == key in invert_dict:
            raise KeyError("Duplicate value has been detected")
        invert_dict[a[key]] = key
    return invert_dict


def count(b: list[str]) -> dict[str, int]:
    """This function produces a dictionary where each key is a unique value in the 
    given list and each value associated is the count of the number of times that value 
    appeared in the input list."""
    count_dict = {}
    for value in b:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


def favorite_color(c:dict[str, str]) -> str:
    """This function returns the color that appears the most frequently in my 
    dictionary. If there is a tie for most popular color, it will return the first 
    color encountered."""
    max_count = 0
    color_count = count(list(c.values()))
    most_frequent = ""

    for value in c.values():
        if color_count[value] > max_count:
            max_count = color_count[value]
            most_frequent = value
    return most_frequent


def bin_len(d:list[str]) -> dict[int, set[str]]:
    """This function bins a list of strings into a dictionary where the key is an int 
    length of a given string and the associated values are a set of strings of the 
    key’s length found in the original list."""
    final_bin = {}

    for value in d:
        length = len(value)
        if length not in final_bin:
            final_bin[length] = set()
        final_bin[length].add(value)
    return final_bin

