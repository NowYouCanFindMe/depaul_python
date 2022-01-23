"""Co Prime - Python3 program
Author: Robert Mwaniki
Date: 1/9/2022
Youtube: https://youtu.be/W71CbKKf6vA

I have not given or received any unauthorized assistance on this assignment.
"""
import sys


def coprime_test_loop():
    """Asks the user for two numbers.

    :rtype: function
    :returns coprime
    """
    a = b = None
    seq = 1
    while True:
        print("*" * 40)
        print("Iteration: {}".format(seq))
        print("*" * 40)
        a, b = evaluate_user_input(get_user_input())
        print("Pair of numbers {} and {} are, ".format(a, b))
        if co_prime(int(a), int(b)):
            print("CoPrime numbers\n")
        else:
            print("Not Coprime numbers\n")
        seq +=1


def co_prime(a, b):
    """Check if two numbers are coprime.

    :param int a: integer value
    :param int b: integer value
    :rtype: bool
    :returns True | False
    """
    divisor = {}

    for i in range(2, a+1):
        mod = (a % i)
        if mod == 0:
            if i in divisor:
                print(divisor)
                return False
            divisor[i] = True

    for i in range(2, b+1):
        mod = (b % i)
        if mod == 0:
            if i in divisor:
                print(divisor)
                return False
            divisor[i] = True
    return True


# helper function
def get_user_input():
    """Get a and b values.

    :rtype: string
    :return: User input as string
    """

    val = input("\nEnter two numbers a, b, or exit() to close. ex 21, 22\n> ")
    return val


# helper function
def evaluate_user_input(val):
    """Evaluate dynamic user input to a standard answer.

    :rtype tuple
    :return: Return tuple of a and b values.
    """
    if val in ('exit()', 'E'): # explit call to exit program
        print("Exiting the program")
        sys.exit()

    if len(val) < 1:
        print("Please enter valid numbers")
        get_user_input()
    else:
        a = None
        b = None
        number_list = val.split(",")

        a = number_list[0]
        b = number_list[1]
    return a, b


def main():
    """Main function."""
    coprime_test_loop()

if __name__ == "__main__":
    main()
