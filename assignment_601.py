"""Assignment601_PalindromeDates - Python3 program
Author: Robert Mwaniki
Date: 2/12/2022
Youtube:

I have not given or received any unauthorized assistance on this assignment.
"""

def get_start_year_of_cent(century):

    if century == 1:
        return 1
    else: 
        return (century - 1) * 100 + 1

def check_if_leap_year(year):
    
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year %4 == 0 and year % 100 != 0:
        return True
    else: 
        return False
     

def check_if_palindrone(date_as_string):
    """Check if String date is a palindrone.
    :param string date_as_string: date as a string

    Returns:
    :return boolean: True or False if palindrone
    """

    # define two pointers at start and end
    i = 0
    j = len(date_as_string)-1
    while i < j:
        if date_as_string[i] != date_as_string[j]:
            return False
        i += 1
        j -= 1

    return True


def validate_day_and_month(day, month, is_leap_yr = False):
    """Validate day and month.

    :param int day: given day
    :param int month: given month

    Returns:
    return: boolean True of False
    """

    months_with_31 = {1, 3, 5, 7, 8, 10, 12}
    months_with_30 = {9, 4, 6, 11}
    months_with_28 = {2}
    
    feb_days = 28
    if is_leap_yr:
        feb_days = 29
    
    if month in months_with_31 and 0 < day <= 31:
        return True
    elif month in months_with_30 and 0 < day <= 30:
        return True
    elif month in months_with_28 and  0 < day <= feb_days:
        return True
    else: 
        return False

def get_century_from_user():
    print("Supports 10th century and up")
    try:
        user_input = input("Enter century i.e. 21\n> ")
        if int(user_input) < 10:
            raise Exception("Invalid century input")
        return int(user_input)
    except:
        print('\nTry again...')
        return get_century_from_user()

def write_to_file(dates):
    with open('palindrone_dates.txt', 'w') as file:
        file.write("*"*10)
        file.write('\n')
        file.write("DD/MM/YYYY\n")
        file.write("*"*10)
        file.write('\n')
        for date in dates:
            file.write(date)
            file.write('\n')

def main():
    """Main function."""
    
    #print(check_if_palindrone("abac"))
    #print(get_start_year_of_cent(14))
    pali_dates = []
    century_input = get_century_from_user()
    start_year = get_start_year_of_cent(century_input)
    end_year = start_year + 100 - 1
    while start_year-1 < end_year: #O(Number of years in a century)
        year = str(start_year)
        #print("Is " + year + " a leap year: " + str(check_if_leap_year(int(year))))
        day = year[2:][::-1] # O(N)
        month = year[:2][::-1] # O(N)
        if validate_day_and_month(int(day), int(month), check_if_leap_year(int(year))) and check_if_palindrone(day+month+year):
            pali_dates.append(day+ "/" + month + "/" + year)
            print(day+ "/" + month + "/" + year)
        start_year+=1
    write_to_file(pali_dates)


if __name__ == "__main__":
    main()

