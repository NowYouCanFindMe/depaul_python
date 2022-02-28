"""Assignment702_Overlapping_Ellipses - Python3 program
Author: Robert Mwaniki
Date: 2/21/2022
Youtube: https://youtu.be/8muILXwkvCc

I have not given or received any unauthorized assistance on this assignment.
"""

import math
import random
import statistics

# pylint: disable=invalid-name
class WarAndPeacePseudoRandomNumberGenerator:
    """Random Number Generator from text file."""
    def __init__(self, seed):
        self.seed = seed
        self.step = 100
        # height of the table
        self.bits = 256 # 32: 6, 16: 5, 8: 4
        self.char_bits = self.get_size_of_bits(self.bits)
        self.list_of_bits = []
        self.random_numbers = []
        self.characters_from_text = {}

    def get_size_of_bits(self, bits):
        """Get size of bits.

        :param int bits: given decimal bits value
        :return int size[bits]: size given bits take
        """
        size = {
            1: 1,
            2: 2,
            4: 3,
            8: 4,
            16: 5,
            32: 6,
            64: 7,
            128: 8,
            256: 9
        }
        return size[bits]

    def random(self):
        """Generate pseudo random numbers"""
        bit_table = []
        holder = [0, 0]
        current_step = char_idx = self.seed

        while char_idx < len(self.characters_from_text):
            if len(bit_table) == self.char_bits:
                self.update_list_of_bits(bit_table)
                # reset bit table
                bit_table = [0, 0]

            if char_idx == current_step:
                binary_in_str = format(ord(self.characters_from_text[char_idx]), '08b')
                #print(binary_in_str)
                # N bits, bit value. i.e. 32, 6th bit value
                val1 = int(binary_in_str[-6])
                holder[0] = val1
                try:
                    val2 = int(format(ord(self.characters_from_text[char_idx]), '08b')[-6])
                    holder[1] = val2
                except Exception:
                    pass
                finally:
                    bit_table.append(val1 & val2)
                    current_step += self.step
                    char_idx = current_step
                    holder = [0, 0]

        print("Generating random values...")
        for list_of_binary in self.list_of_bits:
            #print(list_of_binary)
            running_sum = 0
            div = 1/1
            for num in list_of_binary:
                # r = 1 (1/1) + 1 (1/2) + 1 (1/4) + 0 (1/8) + 0 (1/16) + 1 (1/N number of bits)
                running_sum += num * div
                div *= (1/2)
            self.random_numbers.append(running_sum)

    def get_random(self):
        """Return random numbers."""
        return self.random_numbers

    def get_num_of_random_values(self):
        """Print number of random generated values."""
        print("Number of characters in text file: {}".format(len(self.characters_from_text)))
        print("Number of random values generated: {}".format(len(self.random_numbers)))
        print("Min: {}, Max: {}, and Mean: {}".format(  min(self.random_numbers),
                                                        max(self.random_numbers),
                                                        statistics.mean(self.random_numbers)))

    # helper function
    def open_file(self, file):
        """Open file and read characters.

        :param file file_name: file to open

        Returns:
        :return list char_bits: generated random nums [1,0]
        """
        print("Open File")
        file = open(file, 'r')
        count = 0

        while True:
            # read by character
            char = file.read(1)
            count += 1
            if not char:
                break
            self.characters_from_text[count] = char
        file.close()

    def update_list_of_bits(self, bit_table):
        """Update list of bits.

        :param list bit_table: list binary values from AND operations
        """
        if len(bit_table) == self.char_bits:
            self.list_of_bits.append(bit_table)
        else:
            raise Exception("Bit table did not have {} AND operations".format(self.char_bits))


    def set_bits(self, bits):
        """Update bits.

        :param int bits: user given bits
        """
        self.bits = bits

    def set_step(self, step):
        """Update step

        :param int bits: user given step
        """
        self.step = step

class Point:
    """Point class."""
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def get_x(self):
        """Get X point."""

        return self.x

    def get_y(self):
        """Get Y point."""

        return self.y

class Ellipse:
    """Ellipse class."""
    def __init__(self, p1, p2, w):
        """Ellipse constructor."""
        self.p1 = p1
        self.p2 = p2
        self.w = w
        self.random_points = []

    def get_points(self):
        """Get X, Y points"""
        return self.p1.get_x(), self.p1.get_y(), self.p2.get_x(), self.p2.get_y()

    def get_distance(self, x, pX, y, pY):
        """Get distance of Foci to point in space.
        Known: d1 + d2 = 2a
        Distance: c = sqrt((xA - xB)2 + (yA - yB)2)

        :param int x: x foci point
        :param int y: y foci point
        :param int pX: x point in space
        :param int pY: y point in space

        :return int c: distance between points
        """

        c = math.pow(math.pow(pX - x, 2) + math.pow(pY - y, 2), 0.5)
        return c

    def check_if_valid_point(self, d1, d2):
        """Check if point is valid.
        d1+d2 = 2a
        2a = major axis width (self.w)

        :param int d1: distance of foci 1 to point
        :param int d2: distance of foci 2 to point

        :return boolean: True/False
        """

        if d1+d2 > self.w:
            return False
        return True


def get_rectangle(p1, p2, p3, p4):
    """Get rectangle boundaries.

    :param Point() p1: instance of Point class
    :param Point() p2: instance of Point class
    :param Point() p3: instance of Point class
    :param Point() p4: instance of Point class

    Returns:
    :rtype tuple: l, r, bottom, top, area
    """

    l = min(p1.get_x(), p2.get_x(), p3.get_x(), p4.get_x()) - 2
    r = max(p1.get_x(), p2.get_x(), p3.get_x(), p4.get_x()) + 2
    top = max(p1.get_y(), p2.get_y(), p3.get_y(), p4.get_y()) + 2
    bottom = min(p1.get_y(), p2.get_y(), p3.get_y(), p4.get_y()) - 2
    area = abs(top-bottom) * abs(l-r)

    return l, r, bottom, top, area

def compute_overlap_of_ellipses(random_nums, width, e1, e2, dimensions):
    """Compute overlap of ellipses

    Args:
    :param width int: width
    :param e1 Ellipse(): instance of Ellipse class
    :param e2 Ellipse(): instance of Ellipse class
    :param tuple dimensions: l, r, bottom, top, area
    """
    points = []
    points_e1 = []
    points_e2 = []
    points_overlap = []

    for points in random_nums:
        e1_valid_point = False
        e2_valid_point = False

        pX = points[0]
        pY = points[1]

        # e1
        e1_x1, e1_y1, e1_x2, e1_y2 = e1.get_points()

        e1_d1 = e1.get_distance(e1_x1, pX, e1_y1, pY)
        e1_d2 = e1.get_distance(e1_x2, pX, e1_y2, pY)

        # e2
        e2_x1, e2_y1, e2_x2, e2_y2 = e2.get_points()

        e2_d1 = e2.get_distance(e2_x1, pX, e2_y1, pY)
        e2_d2 = e2.get_distance(e2_x2, pX, e2_y2, pY)

        if e1_d1 + e1_d2 <= width:
            e1_valid_point = True
            points_e1.append([pX, pY])

        if e2_d1 + e2_d2 <= width:
            e2_valid_point = True
            points_e2.append([pX, pY])

        if e1_valid_point and e2_valid_point:
            points_overlap.append([pX, pY])

    area1 = dimensions[4] * (len(points_e1)/10000)
    area2 = dimensions[4] * (len(points_e2)/10000)
    area3 = dimensions[4] * (len(points_overlap)/10000)

    print("Ellipse(Point({},{}), Point({},{}), {}) has area {}".format(e1_x1, e1_y1, e1_x2, e1_y2,width, area1))
    print("Ellipse(Point({},{}), Point({},{}), {}) has area {}".format(e2_x1, e2_y1, e2_x2, e2_y2,width, area2))
    print("The overlap of the two points has an area {}".format(area3))
    print("Points in ellipse 1 {}".format(len(points_e1)))
    print("Points in ellipse 1 {}".format(len(points_e2)))
    print("Points in overlap {}".format(len(points_overlap)))

def generate_random_points(gen_random_nums, random_nums, dimensions):
    """Generate random points

    :param list gen_random_nums: list to hold random [x,y] points
    :param list random_nums: list to hold random_nums
    :param  tuple dimensions: l, r, bottom, top, area - boundaries

    :return list gen_random_nums: list to hold random [x,y] points
    """
    i = 0
    try:
        while len(gen_random_nums) < 10000:
            num = random_nums[i]
            pX = random.randrange(dimensions[0], dimensions[1]-1)+num
            pY = random.randrange(dimensions[2], dimensions[3]-1)+num
            if pX >= dimensions[0] and pX <= dimensions[1] \
                and pY >= dimensions[2] and pY <= dimensions[3]:
                gen_random_nums.append([pX, pY])
            i += 1
        return gen_random_nums
    except:
        return generate_random_points(gen_random_nums, random_nums, dimensions)


def main():
    """Runner function."""
    width = 4
    dimensions = None
    gen_random_nums = []
    # Ellipse 1
    p1 = Point(-1, 2)
    p2 = Point(-2, 3)
    e1 = Ellipse(p1, p2, width)

    # Ellipse 2
    p3 = Point(1, 1)
    p4 = Point(2, 2)
    e2 = Ellipse(p2, p3, width)

    dimensions = get_rectangle(p1, p2, p3, p4)


    seed = 1000 # starting character value
    file_path = 'war-and-peace.txt'
    prng = WarAndPeacePseudoRandomNumberGenerator(seed)
    prng.open_file(file_path)
    prng.random()
    vals = prng.get_random()


    random_nums=generate_random_points(gen_random_nums, vals, dimensions)
    print(len(random_nums))
    compute_overlap_of_ellipses(random_nums, width, e1, e2, dimensions)

if __name__ == "__main__":
    main()