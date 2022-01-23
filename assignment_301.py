"""Assignment301_Goldbach_Conjecture- Python3 program
Author: Robert Mwaniki
Date: 1/23/2022
Youtube: 

I have not given or received any unauthorized assistance on this assignment.
"""

# helper function 
# Run time O(N^2) | space dictionary of O(N) numbers in l,h range
def get_primes(l=4, h=100):
    """Get primes between range.

    :Returns
    :rtype dictionary
    :returns dictionary of primes
    """

    if l > h:
        print_error(l, h)

    primes_dict = {}
    for num in range(l, h + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                # not a prime number if a number other
                # than 1 or itself can divide into it
                # without a remainder
                if (num % i) == 0:
                    break
            else:
                primes_dict[num] = True
    return primes_dict

# helper function
def find_matching_pair(i, primes):
    """Find matching prime pairs.

    :Returns
    :rtype tuple
    :returns matching pair, or 0, 0 if not found

    """
    found_pair = False
    current_val = i
    while not found_pair:
    # 4, 4- 1 = 3, 4-2 = 2    
        current_val -= 1
        possible_value = i -  current_val
        # check to see if there is a matching sum pair
        if possible_value in primes and current_val in primes:
            return possible_value, i-possible_value
        
        # edge case, stop infinite loop
        if possible_value <= 0 or possible_value > i:
            return 0, 0

# helper function
def print_matching_pairs(i, pair_1, pair_2):
    """Print found matching prime pairs."""
    print("{} = {} + {}".format(i, pair_1, pair_2))

# helper function
def print_error(l, h):
    """Print generic error message."""
    print("An error has occured, confirm low and high values: {} and {}.".format(l, h))

def main():
    l = 4
    h = 100
    primes = get_primes(1, h)
    possible_value = 1
    i = l
    while i < h:
        found_pair = False
        current_val = i
        if i < 2: 
            print_error(l, h)
        if i%2 == 0: # is even
            # find matching prime pairs
            pair_1, pair_2 = find_matching_pair(i, primes)
            # print pairs
            if pair_1 > 0 and pair_2 > 0:
                print_matching_pairs(i, pair_1, pair_2)
            i += 1
        else: # not even number
            i += 1


if __name__ == "__main__":
    main()