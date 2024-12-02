# Day 2

def check_monotonic_increase(item: list[int]) -> bool:
    # check if list is monotonic increasing
    return all(item[i] <= item[i+1] for i in range(len(item)-1))

def check_monotonic_decrease(item: list[int]) -> bool:
    # check if list is monotonic decreasing
    return all(item[i] >= item[i+1] for i in range(len(item)-1))

def check_absolute_dif(item: list[int]) -> bool:
    # check if absolute difference is <= 3
     return all(abs(item[i] - item[i+1]) <= 3 for i in range(len(item)-1))


# Part 1
# import data
with open('day2/day2.txt', 'r') as f:
    data = f.read()

# split data in separate lists for each line
items = [line.split(" ") for line in data.splitlines()]
items = [list(map(int, item)) for item in items]

# Retrieve all lists that only contain unique values
unique_items = [item for item in items if len(item) == len(set(item))]

# Check if list is monotonic
increasing = [item for item in unique_items if check_monotonic_increase(item)]
decreasing = [item for item in unique_items if check_monotonic_decrease(item)]

# Check if absolute difference is <= 3
final_inc = [item for item in increasing if check_absolute_dif(item)]
final_dec = [item for item in decreasing if check_absolute_dif(item)]

# get total reports
total = len(final_inc) + len(final_dec)
print(f"Total correct reports is: {total}")


# part 2