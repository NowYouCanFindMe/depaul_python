"""Compute Grade - Python3 program
Author: Robert Mwaniki
Date: 1/9/2022
Youtube: https://youtu.be/3onrvN2QufU

I have not given or received any unauthorized assistance on this assignment.
"""
import sys
from datetime import datetime

CURRENT_YEAR = 2022
MAX_GRADE = 10 # maximum grade a user can acquire


# helper function
def check_file_type():
    """Check if file is a single uncompressed.py file."""
    global MAX_GRADE
    answer = input("\n1. Is the assignment a single uncompressed .py file: (Y/N)\n> ")

    if not evaluate_user_input(answer):
        print("updating max")
        MAX_GRADE = 0 # update global grade
        print_final_grade()


# helper function
def check_for_name_date():
    """Get name from user input."""
    global MAX_GRADE
    answer = input("\n2. Did you include your name and date in assignment (Y/N)\n> ")
    if not evaluate_user_input(answer):
        MAX_GRADE = 0 # update global grade
        print_final_grade()

# helper function
def check_honor_statement():
    """Check if honor statement was included."""
    global MAX_GRADE
    answer = input("\n3. Did you include the honor statement, " \
                   "\n'I have not given or received any unauthorized assistance " \
                   "on this assignment'? (Y/N)\n> ")
    if not evaluate_user_input(answer):
        MAX_GRADE = 0 # update global grade
        print_final_grade()

# helper function
def check_youtube_video():
    """Check unlisted link to Youtube video was included."""
    global MAX_GRADE
    answer = input("\n4. Did you include an unlisted link to a " \
                    "Youtube video presenting the code? (Y/N)\n> ")
    if not evaluate_user_input(answer):
        MAX_GRADE = 0 # update global grade
        print_final_grade()

# helper function
def check_if_on_time():
    """Check if assignment was submitted before due date."""
    val = input ("\n5. Was the assignment submitted before the deadline? (Y/N))\n > ")

    answer = evaluate_user_input(val)

    if not answer:
        check_date()

# helper function
def check_date():
    """Check user provided date, to calculate hours late."""
    global CURRENT_YEAR
    try:
        # get day
        val = input("\ta. What was the day the assignment was submitted ex: 1/6/2022 \n\t> ")
        evaluate_user_input(val) # check if exit command was submitted
        day_split = val.split("/")

        # check year formatting 2022
        if int(day_split[2]) != CURRENT_YEAR:
            raise Exception("Year provided is not valid")

        # get time 00:00 - 23:59
        val = input("\tb. What was the time the assignment was submitted ex: 15:34 \n\t> ")
        evaluate_user_input(val) # check if exit command was submitted
        time_split = val.split(":")

        calculate_hrs_late(day_split, time_split)
    except Exception as exception:
        print("\nAn error occured: {}".format(exception))
        print("Try submitting the day and time again.\n")
        check_date()


# helper function
def calculate_hrs_late(day_split, time_split):
    """Calculate hours late and update global max grade."""
    global MAX_GRADE
    # datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
    sub = datetime(int(day_split[2]),
                   int(day_split[0]),
                   int(day_split[1]),
                   int(time_split[0]),
                   int(time_split[1]),0)
    due = datetime(2022, 1, 10, 23, 59, 0)
    diff = sub - due
    diff_h = diff.total_seconds() / 3600
    hours_late = round(diff_h)

    if hours_late > 0:
        MAX_GRADE = MAX_GRADE - (0.01)*hours_late # update global grade


# helper function
def evaluate_user_input(val):
    """Evaluate dynamic user input to a standard answer.

    :rtype boolean

    Returns:
    :param True - if yes
    :param False - if no

    """
    r_value = None
    if val in ('y', 'Y', 'Yes', 'yes'): # 'y', 'Y', 'Yes', 'yes'
        r_value = True
    elif val in ('n', 'N', 'No', 'no'): # 'n', 'N', 'No', 'no'
        r_value = False
    elif val in ('exit()', 'E'): # explit call to exit program
        print("Exiting the program")
        sys.exit()
    else:
        r_value = False
    return r_value


def print_final_grade():
    """Print final grade and quit program."""
    global MAX_GRADE

    print()
    print("*"*20)
    print("Final Grade: {}".format(MAX_GRADE))
    print("*"*20)
    print()

def help_msg():
    """Help function"""
    print("*" * 40)
    print("Help on running assignment 101")
    print("*" * 40)
    print("Valid arguments: " \
          "\n\tY: yes" \
          "\n\tN: no" \
          "\n\texit(): quit program" \
          "\nOptional keywords:" \
          "\n\tNo, no, n: no" \
          "\n\tYes, yes, y: yes" \
          "\n\tE: exit program"
          )


# main function
def compute_grade():
    """Grading logic

    :rtype int
    :return: Calculated grade the user will get
    """
    global MAX_GRADE
    help_msg()
    # these questions are used to evaluate your grade
    questions = {1: check_file_type, 2: check_for_name_date, 3: check_honor_statement,
                 4: check_youtube_video, 5: check_if_on_time, 6: print_final_grade}
    seq = 1
    while seq < len(questions)+1:

        if MAX_GRADE> 0: # stops additional questions if grade is 0
            questions[seq]()
            seq += 1
        else:
            return MAX_GRADE # break out of loop and return 0

    return MAX_GRADE



if __name__ == "__main__":
    compute_grade()
