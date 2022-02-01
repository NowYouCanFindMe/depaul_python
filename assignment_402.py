"""Assignment402_Human_Pyramid - Python3 program
Author: Robert Mwaniki
Date: 1/30/2022
Youtube: https://youtu.be/AI1WFTFiuTw

I have not given or received any unauthorized assistance on this assignment.
"""

def pyramid (given_weight, row, column):
    """Pyramid of supported weights.

    :param int given_weight: 128
    :param int row: row index
    :param int column: column index
    """
    additional_weight = 128
    if column >= row or column <= 0:
        additional_weight = 0
    if row <= 0 or column < 0 or column > row:
        return 0

    # pylint: disable=line-too-long
    return (additional_weight + given_weight + pyramid (given_weight, row - 1, column - 1) + pyramid (given_weight, row - 1,column))/2
#pylint: enable=line-too-long
def print_all_weights():
    """Print all weights."""
    letters = {'a': (0,0), 'b': (1,0), 'c': (1,1), 'd': (2,0),
               'e': (2,1), 'f': (2,2), 'g': (3,0), 'h': (3,1),
               'i': (3,2), 'j': (3,3), 'k': (4,0), 'l': (4,1),
               'm': (4,2), 'n': (4,3), 'o': (4,4)}
    for letter in letters:
        print("\t" + letter, end=" - ")
        print(pyramid(128, letters[letter][0], letters[letter][1]))

def get_input():
    """Get input from user.

    Returns:
    :rtype: tuple
    :return: row, column values
    """
    user_input = input("Enter row, column values: ")
    row, column = user_input.split(",")
    return int(row), int(column)

def main():
    """Main function."""

    print("*" * 60)
    print("Welcome!\nLetters")
    print_all_weights()
    print("\nEnter row and column values '0, 0' to get supported weight.")
    print("*" * 60)

    row, column = get_input()
    print("Weight supported: ", end=" ")
    print(pyramid(128, row, column))


if __name__ == "__main__":
    main()
