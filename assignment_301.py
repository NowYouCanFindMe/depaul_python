"""Assignment301_Goldbach_Conjecture - Python3 program
Author: Robert Mwaniki
Date: 1/23/2022
Youtube: https://youtu.be/1hPGyTw5avY

I have not given or received any unauthorized assistance on this assignment.
"""

# helper function
# Run time O(N^2) | space dictionary of O(N) numbers in l,h range
def get_primes(lower_bound=4, higher_bound=100):
    """Get primes between range.

    :param int l: lower bound value
    :param int h: upper bound value

    :Returns
    :rtype dictionary
    :returns dictionary of primes
    """

    if lower_bound > higher_bound:
        print_error(lower_bound, higher_bound)

    primes_dict = {}
    for num in range(lower_bound, higher_bound + 1):
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

    :param int i: current value in range loop
    :param dict primes: dictionary of prime values

    :Returns
    :rtype tuple
    :returns matching pair, or 0, 0 if not found

    """
    found_pair = False
    current_val = i
    while not found_pair:
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
    """Print found matching prime pairs.

    :param int i: current i value in range between low and high
    :param int pair_1: matching pair value to sum to i
    :param int pair_2: matching pair value to sum to i
    """
    print("{} = {} + {}".format(i, pair_1, pair_2))

# helper function
def print_error(lower_bound, higher_bound):
    """Print generic error message.

    :param int l: lower bound value
    :param int h: upper bound value
    """
    print("An error has occured, confirm low and "
        "high values: {} and {}.".format(lower_bound, higher_bound))

def main():
    """Find prime sum pairs between range of numbers."""
    lower_bound = 4
    higher_bound = 100
    primes = get_primes(1, higher_bound)
    i = lower_bound
    while i < higher_bound:
        if i < 2:
            print_error(lower_bound, higher_bound)
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
