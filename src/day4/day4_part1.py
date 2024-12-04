import re

with open("src/day4/day4.txt", "r") as f:
    data = f.read().splitlines()


"""
In part 1 we have to find the word XMAS in a word search puzzle
It can be horizontally or vertically or diagonally and reversed
"""
reversedstr = data[::-1]

other_diag = [item[::-1] for item in data]
reversed_other_diag = other_diag[::-1]


def get_diag_elem_top(i, items):
    """
    Get the diagonal elements from the top left to the bottom right
    :param i: The column index
    :param items: The list of strings
    :return: The diagonal elements
    """
    temp = []
    for j, s in enumerate(items):
        if i + j < len(s):
            temp.append(s[i + j])
    return "".join(temp) if temp else temp

def get_diag_elem_bottom(i: int, items: list[str]) -> str:
    """
    Get the diagonal elements from the bottom left to the top right.
    :param i: The column index
    :param items: The list of strings
    :return: The diagonal elements in reverse order
    """
    temp = []
    for j, s in enumerate(items):
        if i - j >= 0:
            temp.append(s[i - j])
    return "".join(reversed(temp)) if temp else temp 


def get_vertical_lines(i: int, items: list[str]) -> str:
    """
    Get the vertical elements from the word search puzzle
    :param i: The column index
    :param items: The list of strings
    :return: The vertical elements
    """
    temp = [item[i] for item in items]
    return "".join(temp) if temp else temp

# we get all the vertical strings
vertical = [get_vertical_lines(i, data) for i in range(len(data[0]))]

# Get Diagonal strings from top left to bottom right
result_diag_1 = [get_diag_elem_top(i, data) for i in range(len(data[0]))]
result_diag_2 = [get_diag_elem_bottom(i, reversedstr) for i in range(len(reversedstr[0]))]
diag_result = list(set(result_diag_1 + result_diag_2))


# Get Diangonal strings from top right to bottom left
result_diag_rev_1 = [get_diag_elem_top(i, other_diag) for i in range(len(other_diag[0]))]
result_diag_rev_2 = [get_diag_elem_bottom(i, reversed_other_diag) for i in range(len(reversed_other_diag[0]))]
other_diag_result = list(set(result_diag_rev_1 + result_diag_rev_2))

# we combine all the strings
validate_list = data + vertical + diag_result + other_diag_result

# find all "xmas" in validate_list
found_xmas = re.findall(r"XMAS", " ".join(validate_list))

# find all "samx" in validate_list
found_samx = re.findall(r"SAMX", " ".join(validate_list))

print(f"total 'XMAS' found: {len(found_xmas) + len(found_samx)}")
