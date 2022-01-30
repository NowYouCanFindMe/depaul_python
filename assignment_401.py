"""Assignment401_Goldbach_Conjecture- Python3 program
Author: Robert Mwaniki
Date: 1/30/2022
Youtube: 

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
    sum = input("Enter a 'sum' value to find: ")
    length = input("Enter a 'length' of random numbers b/w 0 and 100:")

    return sum, length

def generate_random_nums(length):
    """ Generate random numbers.

    :param int: length of list

    Returns: 
    :rtype list
    :return list of random nums
    """
    random_nums = []
    for i in range(length+1):
        get_random = random.randrange(0, 100, 1)
        random_nums.append(get_random)

    return random_nums

def find_sum(sum, random_list):
    """Find possible sum in list of numbers.

    :param int sum: sum we are trying to find
    :param list random_list: randomly generated numbers

    Returns:
    :rtype Boolean
    :return True/False if sum pair is found
    """
    print(random_list)
    # list of unsorted random numbers, sorted
    random_list.sort() # build in n(logn) runtime

    print(random_list)




# main function 
def main(): 
    # get user input
    #sum, length = get_input()
    sum, length = 12, 15
    random_list =  generate_random_nums(length)

    find_sum(sum, random_list)


if __name__ == "__main__":
    main()