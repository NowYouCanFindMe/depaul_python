"""Assignment701_WarAndRandomNum - Python3 program
Author: Robert Mwaniki
Date:
Youtube:

I have not given or received any unauthorized assistance on this assignment.
"""
import statistics


class WarAndPeacePseudoRandomNumberGenerator:
    """Random Number Generator from text file."""
    def __init__(self, seed):
        self.seed = seed
        self.step = 50
        self.bits = 32 # 32: 6, 16: 5, 8: 4
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
            128: 8
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
                # N bits, bit value. i.e. 32, 6th lsb bit value
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
            #print(running_sum)
            self.random_numbers.append(running_sum)

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

def main():
    """Runner function."""
    seed = 1000 # starting character value
    file_path = 'C:\\Users\\rgmwanik\\Documents\\Development\\Python\\Depaul\\depaul_python\\war-and-peace.txt'
    prng = WarAndPeacePseudoRandomNumberGenerator(seed)
    prng.open_file(file_path)
    prng.random()
    prng.get_num_of_random_values()

if __name__ == "__main__":
    main()
