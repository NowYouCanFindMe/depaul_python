"""Assignment302_Happy_Primes - Python3 program
Author: Robert Mwaniki
Date: 1/23/2022
Youtube: https://youtu.be/wi_XCbX1Yl4

I have not given or received any unauthorized assistance on this assignment.
"""
import sys

# max cycles to number to split values, square and find sum
MAX_CYCLES = 10

def print_prime_conditions(start_value, conditions):
    """Prints prime conditions.

    :param int: starting value
    :param  dictionary: conditions
        happy_prime: True
        sad_prime: False
        happy_non_prime: False
        sad_non_prime: False
    """
    output_str = "\n'{}' is a ".format(str(start_value))
    if conditions["happy_prime"]:
        output_str += "Happy Prime"
    if conditions["sad_prime"]:
        output_str += "Sad Prime"
    if conditions["happy_non_prime"]:
        output_str += "Happy Non-Prime"
    if conditions["sad_non_prime"]:
        output_str += "Sad Non-Prime"
    print(output_str)

def validate_input(user_input):
    """Validates user input.

    Returns:
    :rtype bool
    :return true/false if valid input
    """
    try:
        if user_input in ('exit()', 'E'): # explit call to exit program
            print("Exiting the program")
            sys.exit()
        int_val = int(user_input) * 1
        # if int, check if it is negative
        if int_val < 2:
            raise ValueError('Integer should be a positive number, greater than 1.')
        return True
    except Exception as error:
        print("Invalid input. Error: {}".format(error))
        return False

def get_input():
    """Get input from user.

    Returns:
    :rtype int
    :return user input
    """
    user_input = input("\nEnter number: \n> ")
    if validate_input(user_input):
        return int(user_input)
    else:
        # try again
        return get_input()

def split_number(value):
    """Split number and return list.

    Returns:
    :rtype list
    :return num_list: input number partitioned as list
    """
    num_list = []
    while value > 0:
        num_list.append(value %10)
        value = value//10

    return num_list

def sum_of_squares(nums):
    """Find sum of squares.

    :param list nums: partitioned numbers in a list

    Returns:
    :rtype: int
    :return sum of int numbers squared
    """
    # nums is a stack of integers LIFO
    running_sum = 0
    output_str =  ""
    while len(nums) > 1:
        val = nums.pop()
        output_str += str(val) + "^2 + "
        running_sum += val * val

    # last number
    val = nums.pop()
    running_sum += val * val
    output_str += str(val) + "^2 = " + str(running_sum)

    print(output_str)
    return running_sum

def evaluate(starting_num, end_num):
    """Evaluate if number is happy or sad.

    :param int starting_num: starting int value
    :param int end_num: int value at the end of cycles

    Returns:
    :rtype dictionary
    :return dictionary of conditions
    """
    conditions = {
        "happy_prime": False,
        "sad_prime": False,
        "happy_non_prime": False,
        "sad_non_prime": False,
    }

    # end of cycle value is 1, and it is a prime number
    if end_num == 1 and check_if_prime(starting_num):
        conditions["happy_prime"] = True
    # end of cycle value is not 1, and it is a prime number
    elif end_num != 1 and check_if_prime(starting_num):
        conditions["sad_prime"] = True
    # end of cycle value is 1, and it is not a prime number
    elif end_num == 1 and not check_if_prime(starting_num):
        conditions["happy_non_prime"] = True
    # end of cycle value not is 1, and it is not a prime number
    else:
        conditions["sad_non_prime"] = True
    return conditions


def check_if_prime(value):
    """Check if value is a prime number.

    :param int value: given integer value

    :Returns
    :rtype boolean
    :return True/False
    """

    is_prime = True
    for i in range(2, value):
        # not a prime number if a number other
        # than 1 or itself can divide into it
        # without a remainder
        if (value % i) == 0:
            is_prime = False
    return is_prime

# helper function
def help_msg():
    """Help function."""
    print("*" * 40)
    print("Help on running assignment 302")
    print("*" * 40)
    print("Continue to enter integer values, when prompted.")
    print("Valid arguments: " \
          "\n\texit(): quit program" \
          "\n\tE: exit program"
          )

def main():
    """Determine if a number is a happy prime."""

    help_msg()
    while True:
        # get input from user
        input_value = get_input()
        num_as_list = split_number(input_value)
        new_value = sum_of_squares(num_as_list)
        cycles = 0

        # cycles to check if number meets happy conditions
        while new_value > 1 and cycles < MAX_CYCLES:
            num_as_list = split_number(new_value)
            new_value = sum_of_squares(num_as_list)
            cycles += 1
        prime_conditions = evaluate(input_value, new_value)
        print_prime_conditions(input_value, prime_conditions)


if __name__ == "__main__":
    main()
