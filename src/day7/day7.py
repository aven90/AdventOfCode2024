import itertools
import re
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
    tokens = re.findall(r'\d+|\+|\*', expression)
    operator_pos = [i for i, c in enumerate(tokens) if c in ['+', '*']]
    result = 0
    for index, ops in enumerate(operator_pos):
        if index == 0:
            calc = f"{tokens[ops -1]}{tokens[ops]}{tokens[ops + 1]}"
            result = eval(calc)
        else:
            calc = f"{result}{tokens[ops]}{tokens[ops + 1]}"
            result = eval(calc)

    return result

def find_combinations(nums: list[int], target: int) -> bool:
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
    operators = ['+', '*']
    combinations = []
    found_expressions = []

    for ops in itertools.product(operators, repeat=len(nums)-1):
        expression = ''
        for i, num in enumerate(nums):
            expression += str(num)
            if i < len(nums) - 1:
                expression += ops[i]
        result = calc_expression(expression) 
        found_expressions.append(expression)
        if result == target:
            combinations.append(expression)
    if len(combinations) > 0:
        return True
    else:
        return False

correct = []
for test_value, numbers in dataset:
    if find_combinations(numbers, test_value):
        correct.append(test_value)

print(sum(correct))

