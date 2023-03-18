"""Assignment501_Dice_and_cups - Python3 program
Author: Robert Mwaniki
Date: 2/6/2022
Youtube: https://youtu.be/4tCeIGiL2q8

I have not given or received any unauthorized assistance on this assignment.
"""
import random


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
        print(self.sum)
        return self.sum

def main():
    """Runner function."""
    cup = Cup(2, 4, 2)
    cup.roll()
    print("\nSum: ")
    cup.get_sum()

if __name__ == "__main__":
    main()

