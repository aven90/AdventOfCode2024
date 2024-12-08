import re
import itertools
from collections import defaultdict

def _part1_day8(array):
    """
    Identifies unique antinodes in a 2D array of characters.

    An antinode is a point where lines of the same character intersect,
    excluding positions marked by '.'.

    The function calculates the unique antinodes by finding all coordinate
    combinations for each character and checking their validity within the 
    array boundaries.

    :param array: A 2D list of characters representing the map.
    :return: None. Prints the count of unique antinodes found.
    """
    array_len = len(array)
    array_widt = len(array[0])

    # Retrieve unique values in data
    uniques = set()
    for line in array:
        for char in line:
            uniques.add(char)
    uniques.discard('.')

    # Create a dictionary to store the coordinates of each unique character
    coords_dict = defaultdict(list)

    for char in uniques:
        char_coords = []

        for index, line in enumerate(array):
            indexes = [m.start() for m in re.finditer(char, line)]
            for i in indexes:
                char_coords.append((index, i))
        coords_dict[char] = char_coords

    # Create a set to store the antinodes
    antinodes = set()

    # create all combinations for each character
    for char, coords in coords_dict.items():
        # if len(coords) > 1:
        for idx1, idx2 in itertools.combinations(range(len(coords)), 2):
            diff = tuple(a - b for a, b in zip(coords[idx2], coords[idx1]))

            for index, direction in [(idx1, -1), (idx2, 1)]:
                pos = tuple([a+b * direction for a,b in zip(coords[index], diff)])
                if 0 <= pos[0] < array_len and 0 <= pos[1] < array_widt:
                    antinodes.add(pos)
    print(f"Part1: Found unique antinodes: {len(antinodes)}")
        

def _part2_day8(array):

    """
    Finds all antinodes in a given array

    An antinode is a point on the map which is not a node and is not blocked by any node.
    It is the point where two lines of the same character intersect.

    :param array: 2D array of characters
    :return: None
    """
    array_len = len(array)
    array_widt = len(array[0])

    # Retrieve unique values in data
    uniques = set()
    for line in array:
        for char in line:
            uniques.add(char)
    uniques.discard('.')

    # Create a dictionary to store the coordinates of each unique character
    coords_dict = defaultdict(list)

    for char in uniques:
        char_coords = []

        for index, line in enumerate(array):
            indexes = [m.start() for m in re.finditer(char, line)]
            for i in indexes:
                char_coords.append((index, i))
        coords_dict[char] = char_coords

    # Create a set to store the antinodes
    antinodes = set()

    # create all combinations for each character
    for char, coords in coords_dict.items():

        """
        Loop through all combinations of two coordinates of a character and find the 
        antinodes between them
        """
        for idx1, idx2 in itertools.combinations(range(len(coords)), 2):
            diff_y = coords[idx2][0] - coords[idx1][0]
            diff_x = coords[idx2][1] - coords[idx1][1]
            diff = tuple([diff_y, diff_x])

            for index, direction in [(idx1, -1), (idx2, 1)]:
                pos = coords[index]

                # While we are still within the map
                while 0 <= pos[0] < array_len and 0 <= pos[1] < array_widt:
                    antinodes.add(pos) 

                    # we update the position to find the next spot in the line
                    pos = tuple([a+b * direction for a,b in zip(pos, diff)])

    print(f"Part 2: Found unique antinodes: {len(antinodes)}")

# Open data file and split lines
with open("src/day8/input.txt", "r") as f:
    array = f.read().splitlines()

_part1_day8(array)
_part2_day8(array)

