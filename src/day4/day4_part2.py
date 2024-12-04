import re

# open dataset
with open("src/day4/day4.txt", "r") as f:
    data = f.read().splitlines()


"""
Part 2:

It seems we searched the incorrect values
instead of looking for XMAS we need to look for a X shaped MAS
F.E
M _ S
_ A _
M _ S

In each line look for patterns:

1. r"M.S"
2. r".A."
3. r"S.M"
4. r"M.M"
5  r"S.S"

If we find pattern 1, than pattern 2 needs to be in the next line followed by pattern in the following line

If all 3 patterns are found in a line we found a XMAS

Get all patterns, then cross reference the index positions
"""

def find_pattern_occurance(pattern: str, data: list[str]) -> dict[int: list[int]]:
    """
    Finds all occurrences of a given pattern in each line of the provided data.

    Args:
        pattern (str): The regex pattern to search for in the data.
        data (list of str): A list of strings, each representing a line of data.

    Returns:
        dict: A dictionary where the keys are line indices and the values are lists of starting positions
              of the pattern found within each respective line.
    """
    position = {}
    for index, line in enumerate(data):
        patterns = []
        pos = 0
        while True:
            m = re.search(pattern, line[pos:])
            if m is None:
                break
            patterns.append(pos + m.start())
            pos += m.start() + 1
        position[index] = patterns
    return position



m_s_pattern = find_pattern_occurance(r"M.S", data)
a_pattern = find_pattern_occurance(r".A.", data)
s_m_pattern = find_pattern_occurance(r"S.M", data)
m_m_pattern = find_pattern_occurance(r"M.M", data)  
s_s_pattern = find_pattern_occurance(r"S.S", data)

# Now that we have all occurances we can work on the validation part

def check_pattern(pattern1: dict[int: list[int]], pattern2: dict[int: list[int]], pattern3: dict[int: list[int]]) -> int :
    """
    Checks if a pattern is present in the given dictionaries.

    Args:
        pattern1: The first dictionary to search in.
        pattern2: The second dictionary to search in.
        pattern3: The third dictionary to search in.

    Returns:
        int: The number of times the pattern is found.
    """
    count = 0
    for key, val in pattern1.items():
        if key + 2 <= len(pattern1.keys()) -1:
            for item in val:
                if item in pattern2[key+1]:
                    if item in pattern3[key+2]:
                        count += 1
    return count


pattern_comb = [
    (m_s_pattern, a_pattern, m_s_pattern),
    (s_m_pattern, a_pattern, s_m_pattern),
    (m_m_pattern, a_pattern, s_s_pattern),
    (s_s_pattern, a_pattern, m_m_pattern),
]

total_count = sum(map(lambda x:check_pattern(*x), pattern_comb))
print(f"Total 'X-MAS' words found {total_count}")