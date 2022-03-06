"""Assignment901 - Python3 program
Author: Robert Mwaniki
Date: 1/30/2022
Youtube: https://youtu.be/SLuzAdbog9g

I have not given or received any unauthorized assistance on this assignment.
"""

import numpy as np
#from numpy.random import default_rng

def create_random_2d_array(row, column):
    """Create random 2d array

    :param int row: N number of rows
    :param int column: N number of columns
    
    """
    return np.random.rand(row, column)


def create_numpy_1d_array(length, space=1):
    """Use arrange to create a 1d array

    :param int length: size of array
    :param int space: rate to increment by
    :return length
    """
    return np.arange(0,length, space)

def create_linspace_1d_array(length, space=1):
    """Use linspace to create an array

    :param int length: size of array
    :space int space: rate to increment by
    :return array: output array
    """
    return np.linspace(0, length, space)

def create_2d_array_from_1d(array):
    return np.reshape(array, (-1,10))

def question_7(array):
    """Show the results of a[4,5]

    :param array a: array created by numpy arrange
    """
    print("Show the results of a[4 5]")

    print(array[4])

def question_8(array):
    """Show result of a[4]"""
    print("Show the result of a[4]")
    print(array[4])

def question_9(array):
    """Show sum of d"""
    print(np.sum(array))

def question_10(array):
    """Show max of a"""
    print(np.max(array))

def question_11(array):
    """Transpose array b"""
    print(np.transpose(array))

def question_12(array_1, array_2):
    """Add two arrays"""
    print(np.add(array_1, array_2))

def question_13(array_1, array_2):
    """Multiply two arrays"""
    print(np.multiply(array_1, array_2))

def question_14(array_1, array_2):
    """Dot product of two arrays"""
    print(np.dot(array_1, array_2))

def main():
    """Main Runner Fucntion"""

    a = create_numpy_1d_array(100)
    b = create_numpy_1d_array(100, 10)
    c = create_linspace_1d_array(10, 0.1)
    d = create_random_2d_array(10, 10)

    e = create_2d_array_from_1d(a)

    # show a[4,5]
    question_7(e)

    # show the results of a[4]
    question_8(a)

    # show sum of d
    question_9(d)

    # show max of a
    question_10(a)

    #show the transpose of b
    question_11(b)

    # show the results of adding a + d
    question_12(e, d)

    # show the results of multiplying a and d
    question_13(e, d)

    # show the results of computing the dot product of a and b
    question_14(e, b)

    print(e)
if __name__ == "__main__":
    main()