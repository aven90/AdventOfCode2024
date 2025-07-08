tracking = {}

def solution(stone, total_blinks):
    if total_blinks == 0:
        return 1

    if (stone, total_blinks) in tracking:
        # return tracking[(stone, total_blinks)]
        return tracking[(stone, total_blinks)]

    stone_str = str(stone)
    if stone == 0:
        size = solution(1, total_blinks - 1)
    elif len(stone_str) % 2 == 0:
        middle = len(stone_str) // 2
        left = int(stone_str[:middle])
        right = int(stone_str[middle:])
        size = solution(left, total_blinks - 1) + solution(right, total_blinks - 1)

    else:
        size = solution(stone * 2024, total_blinks - 1)

    if (stone, total_blinks) not in tracking:
        tracking[(stone, total_blinks)] = size

    return size


def main():
    with open("src/day11/input.txt", "r") as f:
        data = f.read().split(" ")
    data = list(map(int, data))
    # print(data)
    # part 1
    # solution(data, total_blinks=25)
    total = sum(solution(stone, total_blinks=25) for stone in data)
    print(total)
    
    # part 2
    total = sum(solution(stone, total_blinks=75) for stone in data)
    print(total)

if __name__ == "__main__":
    main()