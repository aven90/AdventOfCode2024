import time
from functools import cache

"""
Day 11 we are on Pluto

We see a set of physics-defying stones
they're in a straight line and have a number

each time we blink:
- a stone splits in 2, shifting the others to form the straight line
- the number changes

After observation we find that the stones change simultaneously
- if the stone is engraved with 0, it is replaced with 1
- if the has even numbers (length is even)   the stones split f.e. 1000 become 10 | 0
- else: the stone is replaced with number * 2024

The order is preserved

how many stones will be there after 25 blinks (iterations)
"""

stone_cache = {}

def solution(stone: int, blinks: int):
    """
    This function calculates the total number of stones after a given number of blinks.

    The function takes two parameters: the current stone number and the number of blinks.
    The function is recursive and uses memoization to store the results of subproblems.
    The function returns the total number of stones after the given number of blinks.

    The algorithm works as follows:
    1. If the number of blinks is 0, the function returns 1 (as there is only one stone).
    2. If the new stone is already calculated, the function returns the result from the cache.
    3. Else, the function calculates the new stone and keeps calculating until the number of blinks is 0.
    4. Each time the function is called, the number of blinks is reduced and the number of stones increases with 1 as a counter.
    5. The function then stores the new stone in the cache.
    6. Finally, the function returns the count of new stones.
    """

    # define basic case scenario
    if blinks == 0:
        return 1

    # if new stone is already calculated, return result from cache
    if (stone, blinks) in stone_cache.keys():
        return stone_cache[(stone, blinks)]

    # else we calculate new stone, and keep calculating until blinks == 0
    # each time the function is called, the blinks are reduced and new stone increases with 1 as a counter
    stone_str = str(stone)
    if stone == 0:
        num_stones = solution(1, blinks - 1)
    elif len(stone_str) % 2 == 0:
        middle = len(stone_str) // 2
        left = int(stone_str[:middle])
        right = int(stone_str[middle:])
        num_stones = solution(left, blinks - 1) + solution(right, blinks - 1)
    else:
        num_stones = solution(stone * 2024, blinks - 1)
    
    # store new stone in cache
    if (stone, blinks) not in stone_cache.keys():
        stone_cache[(stone, blinks)] = num_stones

    # then return the count of new_stones
    return num_stones

@cache
def solution_cache_improved(stone: int, blinks: int):
    """
    This function calculates the total number of stones after a given number of blinks.

    The function takes two parameters: the current stone number and the number of blinks.
    The function is recursive and uses memoization to store the results of subproblems.
    The function returns the total number of stones after the given number of blinks.

    The algorithm works as follows:
    1. If the number of blinks is 0, the function returns 1 (as there is only one stone).
    2. If the new stone is already calculated, the function returns the result from the cache.
    3. Else, the function calculates the new stone and keeps calculating until the number of blinks is 0.
    4. Each time the function is called, the number of blinks is reduced and the number of stones increases with 1 as a counter.
    5. The function then stores the new stone in the cache.
    6. Finally, the function returns the count of new stones.
    """

    # define basic case scenario
    if blinks == 0:
        return 1

    # else we calculate new stone, and keep calculating until blinks == 0
    # each time the function is called, the blinks are reduced and new stone increases with 1 as a counter
    stone_str = str(stone)
    if stone == 0:
        num_stones = solution(1, blinks - 1)
    elif len(stone_str) % 2 == 0:
        middle = len(stone_str) // 2
        left = int(stone_str[:middle])
        right = int(stone_str[middle:])
        num_stones = solution(left, blinks - 1) + solution(right, blinks - 1)
    else:
        num_stones = solution(stone * 2024, blinks - 1)

    # return the count of new_stones
    return num_stones
    

def main():
    with open("src/day11/input.txt", "r") as f:
        data = f.read().split(" ")
    data = list(map(int, data))

    start = time.time()
    # Part 1 blinks = 25, Part 2 blinks = 75
    total_stones = [solution(stone, blinks=75) for stone in data]
    total_stones = [solution_cache_improved(stone, blinks=75) for stone in data]
    print(sum(total_stones))
    end = time.time()
    print(f"Total runtime is: {end - start} seconds")


if __name__ == "__main__":
    main()