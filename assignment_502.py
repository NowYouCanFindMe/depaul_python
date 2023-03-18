"""Assignment502_Cups_and_Dice - Python3 program
Author: Robert Mwaniki
Date: 2/6/2022
Youtube: https://youtu.be/1YpkKB_Dh_0

I have not given or received any unauthorized assistance on this assignment.
"""
import random
import time

class SixSidedDie:
    """Base Die Class."""
    def __init__(self, sides):
        self.face_value = None
        self.sides = sides

    def set_sides(self, sides):
        """Set sides of die."""
        self.sides = sides

    def roll(self):
        """Roll the die."""
        self.face_value = random.randrange(1, self.sides)
        print("{} sided die - {}".format(self.sides, self.face_value))
        return self.get_face_value()

    def get_face_value(self):
        """Return self face value

        Returns:
        :return int face_value: dice face value
        """
        return self.face_value

    def __repr__(self):
        """Formal representation."""
        return "SixSidedDie({})".format(self.sides)


class TenSidedDie(SixSidedDie):
    """Abstract class inherits SixSidedDie."""



class TwentySidedDie(SixSidedDie):
    """Abstract class inherits SixSidedDie."""



class Cup:
    """Cup class to hold the Dice."""
    def __init__(self, num_of_6_side, num_of_10_side, num_of_20_side):
        self.num_of_6_side = num_of_6_side
        self.num_of_10_side = num_of_10_side
        self.num_of_20_side = num_of_20_side
        self.sum = 0

    def roll(self):
        """Roll the die."""
        running_sum = 0
        if self.num_of_6_side:
            die = SixSidedDie(6)
            print("\n" + repr(die))
            for _ in range(self.num_of_6_side):
                running_sum += die.roll()

        if self.num_of_10_side:
            die = SixSidedDie(10)
            print("\n" + repr(die))
            for _ in range(self.num_of_10_side):
                running_sum += die.roll()

        if self.num_of_20_side:
            die = SixSidedDie(20)
            print("\n" + repr(die))
            for _ in range(self.num_of_20_side):
                running_sum += die.roll()
        self.sum = running_sum

    def get_sum(self):
        """Returns sum of die faces in the cup."""
        print("\nTotal sum is {}".format(self.sum))
        return self.sum


class User:
    """User class to hold user data."""
    def __init__(self):
        self.name = None
        self.balance = 100
        self.bet = 0
        self.last_roll = None
        self.play_state = False
        self.goal = random.randrange(1, 100)

    def generate_new_goal(self):
        """Generate a new goal if user won last roll."""
        self.goal = random.randrange(1, 100)

    def play_game(self, state):
        """Start or stop the game"""
        self.play_state = state

    def game_in_progress(self):
        """Check if game in progress.

        Returns:

        rtype: Boolean
        :returns boolean True/False
        """
        return self.play_state

    def set_user_name(self, name):
        """Set user name.
        :param str name: entered user's name
        """
        self.name = name

    def get_user_name(self):
        """Get user name.

        Returns:
        :return str self.name: user name
        """
        return self.name

    def get_goal(self):
        """Get user goal.

        Returns:
        :return int self.goal: goal to try to roll to
        """
        return self.goal

    def set_last_roll(self, roll):
        """Set last roll

        :param: int roll
        """
        self.last_roll = roll

    def get_last_roll(self):
        """Get last roll"""
        return self.last_roll

    def set_bet(self, money):
        """Set bet.

        :param int money: user's bet
        """
        self.bet = money
        self.make_bet()

    def make_bet(self):
        """Deduct bet from balance"""
        self.balance -= self.bet

    def get_user_balance(self):
        """Get user balance.

        Returns:
        :return int self.balance: remaining user balance
        """
        return self.balance

    def update_user_balance(self):
        """Update user balance."""

        if self.last_roll == self.goal:
            self.balance += self.bet * 10
        # within 3 feet and under
        elif self.goal-self.last_roll <= 3 and self.last_roll < self.goal:
            self.balance += self.bet * 5
        # within 10 feet and under
        elif self.goal-self.last_roll <= 10 and self.last_roll < self.goal:
            self.balance += self.bet * 2
        else:
            pass
        print("Current Balance: ${}".format(self.balance))


def continue_playing():
    """Ask user to continue player."""
    next_round = input("Play again? 'Y' or 'N' \n> ")
    if next_round in ('Y', 'yes', 'yep', 'y', 'Yes'):
        return True
    return False

def get_number_of_die():
    """Get number of die."""
    try:
        user_input = input("Enter three numbers i.e 3, 4, 1 \n> ")
        input_split = user_input.split(",")
        print(input_split)
        return int(input_split[0]), int(input_split[1]), int(input_split[2])
    except:
        print("Invalid input. Try again.\n")
        return get_number_of_die()

def get_bet_from_user(current_balance):
    """Get bet from user

    :params int current_balance: user's balance
    :returns int value: bet from user
    """
    try:
        bet = input("How much would you like to bet?\n> ")
        value = int(bet)
        if value < 0 or value > current_balance:
            raise Exception("The value is below '0'")
        return value
    except:
        print("Invalid bet. Try again.\n")
        return get_bet_from_user(current_balance)

def greet_user(name, goal):
    """Greet User.

    :param str name: user's name
    :param int goal: target goal
    """
    print("\nDo you feel lucky, {}?\nThe goal to reach is {}, can you roll and make the $$bankroll$$.".format(name, goal))
    print("Enter # number of six sided die, number of 10 sided die, and number of 20 sided die")

def main():
    """Runner function."""
    user = User()
    entered_name = input("Enter your name: ")

    user.set_user_name(entered_name)
    user.play_game(True)
    while user.game_in_progress():
        old_balance = user.get_user_balance()
        greet_user(user.get_user_name(), user.get_goal())
        bet = get_bet_from_user(old_balance)
        user.set_bet(bet)
        num_1, num_2, num_3 = get_number_of_die()
        cup = Cup(num_1, num_2, num_3)
        print("Rolling...")
        time.sleep(1)
        cup.roll()
        user.set_last_roll(cup.get_sum())
        user.update_user_balance()
        if old_balance < user.get_user_balance():
            print("\nCongrats {}! You have increased your balance to {}".format(user.get_user_name(), user.get_user_balance()))
            user.generate_new_goal()
        else:
            print("\nDarn {}! Maybe next time. You were {} away from the goal.".format(user.get_user_name(), abs(user.get_goal() - user.get_last_roll())))
            if user.get_user_balance() <= 0:
                print("Maybe gambling is not for you {}. You ran out of money.".format(user.get_user_name()))
                break

        # check to see if user wants to play again
        user.play_game(continue_playing())


if __name__ == "__main__":
    main()
