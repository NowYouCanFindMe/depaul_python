"""Assignment202_Stem and Leaf creator - Python3 program
Author: Robert Mwaniki
Date: 1/17/2022
Youtube: https://youtu.be/txkGysbE2Io

I have not given or received any unauthorized assistance on this assignment.
"""
import sys
import os


# helper function
def greet_user():
    """Greet User."""
    print("*" * 80)
    print("*\tHello user!\n*\tThis program will create a stem and leaf histogram.")
    print("*" * 80)
    print()

# helper function
def get_input(data_files):
    """Get user input
    :rtype string

    Returns:
    :rtype string
    :return user inputted file number

    """
    print("*" * 40)
    for key, value in enumerate(data_files):
        print("Input '{}' for {}.txt".format(key+1, value))
    print("Type exit(), or 'E' to exit.")
    print("*" * 40)
    file_number = None
    while not file_number:
        file_number = input("\nWhat is the file number you want to open? Type 'exit()' to close.\n> ")
        if file_number in ('exit()', 'E'): # explit call to exit program
            print("Exiting the program")
            sys.exit()
    return file_number

# helper function
def open_file(file_name):
    """Open File in current directory.

    :param str file_name: file name to open

    :Returns
    :rtype dictionary
    :return unsorted dictionary of stem leaf pairing.
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = current_dir +"\\"+ file_name+".txt"
    unsorted_dict = {}
    infile = open(filename, "r")
    lineList = infile.readlines()
    infile.close()
    for i in range ( 0, len(lineList) ):
        number_string = lineList[i].strip()
        if not int(number_string[0:-1]) in unsorted_dict:
            unsorted_dict[int(number_string[0:-1])] = [int(number_string) % 10]
        else:
            curr_numbers = unsorted_dict[int(number_string[0:-1])]
            curr_numbers.append(int(number_string) % 10)
            unsorted_dict[int(number_string[0:-1])] = curr_numbers
        print (number_string)
    return unsorted_dict

# helper function
def check_if_file_valid(input, data_files):
    """Check if file name exists

    :param str input: user input
    :param list data_files: list of files

    :Returns
    :rtype int
    :param file_index

    """
    try:
        idx = int(input)
        if data_files[idx-1]:
            return idx-1
    except Exception as error:
        print("Error occured: {}".format(error))
        print("Try again...")

# helper function
def print_output(sorted_dict):
    """Print out sorted dictionary of stem and leaves.

    :param dictionary sorted_dict: sorted stem with leaves

    """
    print("*" * 40)
    print("Stem and Leaf plot")
    print("*" * 40)
    for key, value in sorted_dict.items():   
        number_list = "" # leafs as string
        value.sort() # sort leafs in ascending order
        for leaf in value:
            number_list += " " + str(leaf)
        print(str(key) + " : " + number_list)

# main function
def main():
    """Read in file data and print stem file
    """
    data_files = ["StemAndLeaf1", "StemAndLeaf2", "StemAndLeaf3"]
    greet_user()
    file_idx = None
    while True:
        file_number = get_input(data_files)
        # pass in file name
        file_idx = check_if_file_valid(file_number, data_files)
        if file_idx != None:
            # get unsorted stem and leaf dictionary and sort by key
            unsorted_dict = open_file(data_files[file_idx])
            sorted_dict = dict(sorted(unsorted_dict.items()))
            print_output(sorted_dict)


if __name__ == "__main__":
    main()
