# Day 2
def check_monotonic_and_range(item: list[int]) -> bool:
    return (
        all(item[i] <= item[i+1] for i in range(len(item)-1)) or
        all(item[i] >= item[i+1] for i in range(len(item)-1))
        ) and all(1 <=abs(item[i] - item[i+1]) <= 3 for i in range(len(item)-1))



# Part 1
# import data
with open('src/day2/day2.txt', 'r') as f:
    data = f.read()

# split data in separate lists for each line
items = [line.split(" ") for line in data.splitlines()]
items = [list(map(int, item)) for item in items]

total = sum(map(check_monotonic_and_range, items))

print(f"Total part1 correct reports is: {total}")


# part 2
new_total = 0
# loop over all items in the list
for item in items:
    # check if the current item is valid
    # if not, check if any of the items without one element is valid
    new_total += check_monotonic_and_range(item) \
    or any(check_monotonic_and_range(item[:i] + item[i+1:]) for i in range(len(item)))

# print the total number of valid reports
print(f"Total new correct reports is: {new_total}")

