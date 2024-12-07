import itertools
import re
import time
"""
We get a list of values split by :
before : is the end value
after : need to be used to calculate the total
Only addition and multiplication is allowed

"""

with open("src/day7/input.txt", "r") as f:
    data = f.read().splitlines()

dataset = []
# print(len(data))
for line in data:
    test_vals, nums = line.split(":")
    nums = list(map(int, nums.split()))
    dataset.append([int(test_vals), nums])


# print(dataset)

def calc_expression(expression:str) -> int:
    """
    Calculate the result of the expression by applying the + and * operators.
    
    The expression is a string that contains the numbers and operators separated by spaces.
    The method works by iterating over the operators and applying them to the running result.
    The result is then returned.
    """
    # adjust operatrs for part 2
    tokens = re.findall(r"(\d+|\|\||\*|\+)", expression)
    operator_pos = [i for i, c in enumerate(tokens) if c in ['+', '*', '||']]
    result = 0
    for index, ops in enumerate(operator_pos):
        # if the operator is ||, we concatonate the 2
        if tokens[ops] == '||':
            if index == 0:
                calc = f"{tokens[ops - 1]}{tokens[ops + 1]}"
                result = int(calc)
            else:
                calc = f"{result}{tokens[ops + 1]}"
                result = int(calc)
        else: 
            if index == 0:
                calc = f"{tokens[ops - 1]}{tokens[ops]}{tokens[ops + 1]}"
                result = eval(calc)
            else:
                calc = f"{result}{tokens[ops]}{tokens[ops + 1]}"
                result = eval(calc)

    return result

def find_combinations(nums: list[int], target: int, part: str) -> bool:
    """
    Find all combinations of + and * operators that can be used to connect
    a list of numbers to get a certain target value.

    Args:
        nums (list): The list of numbers
        target (int): The target value

    Returns:
        list: A list of strings, where each string is an expression that
        evaluates to the target value
    """
    # added || for part 2 to operators
    if part =="part2":  
        operators = ['+', '*', '||']
    else:
        operators = ['+', '*']

    for ops in itertools.product(operators, repeat=len(nums)-1):
        expression = ''
        for i, num in enumerate(nums):
            expression += str(num)
            if i < len(nums) - 1:
                expression += ops[i]
        # print(expression)
        result = calc_expression(expression) 

        if result == target:
            return True

    return False

correct = []
for i, val in enumerate(dataset):
    print(f"{i+1}/{len(dataset)}, {val[0]}")
    if find_combinations(val[1], val[0], "part1"):
        correct.append(val[0])

print(sum(correct))

# added validation for part 2 changes, to know base logic still is correct
try:
    assert sum(correct) == 4555081946288
    # assert sum(correct) == 3749  # example input
    print("Part 1 still okay")
except AssertionError:
    print("Part 1 failed")


"""
for part 2 we get an extra operator ||
|| is concatenate
we adjust the calculation function and find combination function to handle this operator
"""
correct = []
for i, val in enumerate(dataset):
    print(f"{i+1}/{len(dataset)}, {val[0]}")
    if find_combinations(val[1], val[0], "part2"):
        correct.append(val[0])

print(sum(correct))

# check for refactor after solving
try:
    assert sum(correct) == 227921760109726
    # assert sum(correct) == 11387   # example input
    print("Part 2 still okay")
except AssertionError:
    print("Part 2 failed")

