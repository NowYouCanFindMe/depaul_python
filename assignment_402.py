"""Assignment402_Human_Pyramid - Python3 program
Author: Robert Mwaniki
Date: 1/30/2022
Youtube:

I have not given or received any unauthorized assistance on this assignment.
"""
def pyramid(row, column, matrix, weight):
    """Human Pyramid

    :param int row: row index
    :param int column: column index
    :param float weight: supported weight
    """
    if row > 4 or column > 4: # letter P and greater
        return matrix
    # update supported weight
    print("{} {}".format(row, column))
    curr_weight = weight + 128
    print("Weight" + str(curr_weight))
    matrix[row][column] += weight + 128
    
    #print(matrix)
 
    # divide weight with left and right children
    half = matrix[row][column] //2

    pyramid(row+1, column, matrix, half)
    pyramid(row+1, column+1, matrix, half)
    return matrix

def weight_on (r,c):
    
    second_person = 128 #finds out if there is a second person on top or not
    if c - 1 < 0 or c > r - 1 :
        second_person = 0
    if c < 0 or c > r:
        return 0
    elif r <= 0:
        return 0
    else:
        return (second_person + 128 + weight_on (r - 1,c - 1) + weight_on (r - 1,c))/2

def main():
    """Main function."""
    num_letters = 26
    
    matrix = [[0 for _ in range(num_letters)] for _ in range(num_letters)]
    #print(matrix)
    weight = 128
    row = 0
    column =  0
    alpha_idx = 0 # 'A'
    print(weight_on(4, 2))
    # matrix = pyramid(row, column, matrix, 0)
    # for row in matrix:
    #     print(row)
    # m = 400
    # J = 112

if __name__ == "__main__":
    main()

