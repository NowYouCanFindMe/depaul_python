"""Assignment401_Goldbach_Deuce - Python3 program
Author: Robert Mwaniki
Date: 1/30/2022
Youtube: https://youtu.be/SLuzAdbog9g

I have not given or received any unauthorized assistance on this assignment.
"""

import random

# helper function
def get_input():
    """Get user input.

    Returns:
    :rtype tuple
    :return sum, length
    """
    given_sum = input("Enter a 'sum' value to find: ")
    length = input("Enter a 'length' of random numbers to generate: ")

    return int(given_sum), int(length)

def generate_random_nums(length):
    """ Generate random numbers.

    :param int: length of list

    Returns:
    :rtype list
    :return list of random nums
    """
    random_nums = []
    for _ in range(length+1):
        get_random = random.randrange(0, 100, 1)
        random_nums.append(get_random)

    return random_nums

def find_sum(given_sum, random_list):
    """Find possible sum in list of numbers.

    :param int sum: sum we are trying to find
    :param list random_list: randomly generated numbers

    Returns:
    :rtype Boolean
    :param True - if found
    :param False - if not found
    """
    # list of unsorted random numbers, sorted
    random_list.sort() # build in sort n*log(n) runtime
    idx = 0
    while idx < len(random_list):
        val = random_list[idx]
        # find possible sum
        # sum = val + possible_val
        possible_val = given_sum - val
        # for each value in random_list, do binary search to find sum pair
        # n*log(n)
        if binary_search(possible_val, random_list):
            print("{} = {} + {}".format(given_sum, val, possible_val))
            return True
        # increase idx and look for next possible pair
        idx += 1
    # return false if no possible pair equals sum
    return False

def binary_search(search_val, sorted_list):
    """Binary search, O(logN)

    :param int search_val: pair we are trying to find
    :param list sorted_list: sorted list of random nums

    Returns:
    :rtype Boolean
    :param True - if found
    :param False - if not found
    """
    left = 0
    right = len(sorted_list)-1

    while left <= right:
        mid = (left+right) //2
        if search_val < sorted_list[mid]:
            # search left
            right = mid-1
        elif search_val > sorted_list[mid]:
            # search right
            left = mid + 1
        else:
            # search_val is mid value
            return True
    # not found
    return False

# main function
def main():
    """Main function."""
    # get user input
    given_sum, length = get_input()
    #given_sum, length = 20, 100
    random_list =  generate_random_nums(length)

    if not find_sum(given_sum, random_list):
        print("The sum of '{}' was not found in a random list".format(given_sum), end=" ")
        print("of length '{}'.".format(length))


if __name__ == "__main__":
    main()
