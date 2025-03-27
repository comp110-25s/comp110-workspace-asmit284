"""The purpose of this exercise is to  implement a main function that contains Wordle's “game loop”."""

__author__: str = "730548173"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_str: str, answer_str: str) -> bool:
    """This function checks if a specific character in the second string is found at any index of the first string"""

    assert len(answer_str) == 1, f"len('{answer_str}') is not 1"
    return answer_str in search_str


def emojified(guess: str, secret: str) -> str:
    """This function will return a string of emoji whose color codifies the results of a guess using Wordle's logic"""

    assert len(guess) == len(secret), "Guess must be same length as secret"

    result = ""
    idx = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1

    return result


def input_guess(expected_length: int) -> str:
    """This function will prompt the user for a guess and continue prompting them"""
    """until they provide a guess of the expected length."""

    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turns = 1
    total_turns = 6
    won = False

    while turns <= total_turns and not won:
        print(f"=== Turn {turns}/{total_turns} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True
        else:
            turns += 1

    if won:
        print(f"You won in {turns}/{total_turns} turns!")
    else:
        print(f"X/{total_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
