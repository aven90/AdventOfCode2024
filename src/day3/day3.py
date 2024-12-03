import re

def extract_and_mulitply_from_mull(str):
    # passed string is a mull like (mul(1,2,))
    # extract the numbers
    # multiply them
    # return the result
    numbers = re.findall(r"\d+", str)   
    return int(numbers[0]) * int(numbers[1])

# part 1
"""
In part 1 we need to extract all mulls from the memory and multiply the numbers inside
We can ignore everything that doesn't fit the pattern
"""
# open data
with open("src/day3/input.txt", "r") as f:
    data = f.read()

# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# define pattern
pattern = r"mul\(\d+,\d+\)"

# find all muls in data fitting the pattern
found_mulls = re.findall(pattern, data)

# we calculate the total
total = sum(map(extract_and_mulitply_from_mull, found_mulls))

print(f"Total part1 correct reports is: {total}")

# part 2
"""
In part 2 we discovered that the memory string contains logic.
It containts 2 functions: do()_mul and don't()_mul

Everything after don't() is disabled and should not be considered
Everythin after do() is enabled and should be considered
Everything before the first don't is considere enabled
"""

dont_start_indexes = [m.start() for m in re.finditer(r"don't\(\)", data)]
do_start_indexes = [m.start() for m in re.finditer(r"do\(\)", data)]
combined_start_indexes = sorted(dont_start_indexes + do_start_indexes)

donts= []
dos = [] 
first_slice = data[:combined_start_indexes[0]]

for i, v in enumerate(combined_start_indexes):
    subslice = data[v:combined_start_indexes[i+1]] if i < len(combined_start_indexes) -1 else data[v:]
    (donts if v in dont_start_indexes else dos).append(subslice)

new_data = first_slice + "".join(dos)
found_mulls = re.findall(pattern, new_data)

total = sum(map(extract_and_mulitply_from_mull, found_mulls))

print(f"Total part2 correct reports is: {total}")

