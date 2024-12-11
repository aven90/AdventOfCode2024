def part1(data):

    """
    Processes input data to create a list `datalist` by alternating between appending numbers and dots.
    Then, rearranges the list so that all numbers appear before dots, maintaining the order of numbers.
    Finally, calculates and prints the weighted sum of indices where numbers are located.

    Args:
        data (list of str): A list where each element is a string representation of a number.
    """
    datalist = []
    x = 0
    for index, val in enumerate(data):
        if index % 2 == 0:
            for i in range(int(val)):
                datalist.append(str(x))
            x += 1
        else:
            for _ in range(int(val)):
                datalist.append(".")
    # print(datalist)

    next_free = datalist.index(".")
    numbs = []
    for i, val in enumerate(datalist):
        if val.isdigit():
            numbs.append(i)

    while next_free < numbs[-1]:
        datalist[next_free], datalist[numbs[-1]] = datalist[numbs[-1]],datalist[next_free]

        next_free = datalist.index(".")
        numbs = []
        for i, val in enumerate(datalist):
            if val.isdigit():
                numbs.append(i)
  

    # # print(compressed_ds)
    total = []
    for index, val in enumerate(datalist):
        if val == ".":
            continue
        else:
            total.append(index*int(val))

    print(sum(total))


def main():

    file = "input"
    with open(f"src/day9/{file}.txt", "r") as f:
        data = f.read()
    # data = "12345"
    part1(data)

if __name__ == "__main__":
    main()