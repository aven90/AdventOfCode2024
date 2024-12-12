import numpy as np

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

def solution(data: list[int], total_blinks: int):
    print(data)
    stones = np.array(data, dtype=int)
    print(type(stones))
    blinks = 0
    while blinks < total_blinks:
        print(F"blinked {blinks} of {total_blinks}, now have {len(stones)} stones")
        new_order = []

        for stone in stones:
            stone_str = str(stone)
            if stone == 0:
                new_order.append(1)
            elif len(stone_str) % 2 == 0:
                middle = len(stone_str) // 2
                left = int(stone_str[:middle])
                right = int(stone_str[middle:])
                new_order.extend([left, right])

            else:
                new_num = stone * 2024
                new_order.append(new_num)

        blinks += 1
        stones = np.array(new_order, dtype=int)
    # print(stones_iteration)
    total_stones = len(stones)
    print(f"Found {total_stones} stones after {total_blinks} blinks")
    

def main():
    with open("src/day11/input.txt", "r") as f:
        data = f.read().split(" ")
    data = list(map(int, data))
    # print(data)
    # part 1
    solution(data, total_blinks=75)
    
    # part 2
    # solution(data, total_blinks=75)


if __name__ == "__main__":
    main()