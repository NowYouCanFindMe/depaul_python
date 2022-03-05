"""Assignment402_Human_Pyramid - Python3 program
Author: Robert Mwaniki
Date: 1/30/2022
Youtube:

I have not given or received any unauthorized assistance on this assignment.
"""
matrix = [[128 for _ in range(26)] for _ in range(26)]
def pyramid(row, column, weight, shoulders):
    """Human Pyramid

    :param int row: row index
    :param int column: column index
    :param float weight: supported weight
    """
    global matrix
    if row == 0 and column == 0:
        weight[row][column] = 0

    if row > 5 or column > 5:
        return
    


    weight[row][column] += shoulders
    pyramid(row+1, column, weight, shoulders + 64)
    pyramid(row+1, column+1, weight, shoulders + 64)
  

  


   
    return weight

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
    
    
    weight = [[0 for _ in range(num_letters)] for _ in range(num_letters)]
    #print(matrix)
    weight = 128
    row = 0
    column =  0
    alpha_idx = 0 # 'A'
    #print(weight_on(4, 2))
    matrix = pyramid(row, column, weight, 0)
    for row in matrix:
        print(row)
    # m = 400
    # J = 112

if __name__ == "__main__":
    main()

