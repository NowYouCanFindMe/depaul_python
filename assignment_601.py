"""Assignment601_PalindromeDates - Python3 program
Author: Robert Mwaniki
Date: 2/14/2022
Youtube: https://youtu.be/loQMwTJGNSk

I have not given or received any unauthorized assistance on this assignment.
"""

def get_start_year_of_cent(century):
    """Get starting year of the century.

    :param int century: given century

    Returns:
    return: int century: start year
    """

    if century == 1:
        return 1
    return (century - 1) * 100 + 1

def check_if_leap_year(year):
    """"Check if year is a leap year.

    :param int year: given year
    """

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    if year %4 == 0 and year % 100 != 0:
        return True

    return False


def check_if_palindrome(date_as_string):
    """Check if String date is a palindrone.
    :param string date_as_string: date as a string

    Returns:
    :return boolean: True or False if palindrone
    """

    # define two pointers at start and end
    start_idx = 0
    end_idx = len(date_as_string)-1
    while start_idx < end_idx:
        if date_as_string[start_idx] != date_as_string[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1

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
    if month in months_with_30 and 0 < day <= 30:
        return True
    if month in months_with_28 and  0 < day <= feb_days:
        return True
    
    return False

def get_century_from_user():
    """Get user input.

    Returns:
    :return int user_input: century as string
    """
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
    """Write to text file."""
    with open('palindrome_dates.txt', 'w') as file:
        file.write("*"*10)
        file.write('\n')
        file.write("DD/MM/YYYY\n")
        file.write("*"*10)
        file.write('\n')
        for date in dates: # O(N)
            file.write(date)
            file.write('\n')

def main():
    """Main function."""

    pali_dates = []
    century_input = get_century_from_user()
    start_year = get_start_year_of_cent(century_input)
    end_year = start_year + 100 - 1
    while start_year < end_year: # O(Number of years in a century)
        year = str(start_year)
        day = year[2:][::-1] # O(N)
        month = year[:2][::-1] # O(N)
        if validate_day_and_month(int(day), int(month), check_if_leap_year(int(year))) and check_if_palindrome(day+month+year):
            pali_dates.append(day+ "/" + month + "/" + year)
            print(day+ "/" + month + "/" + year)
        start_year+=1
    write_to_file(pali_dates)


if __name__ == "__main__":
    main()
